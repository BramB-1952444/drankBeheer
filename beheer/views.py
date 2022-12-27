import json
from django.db.models.deletion import ProtectedError
from django.db.models.expressions import ExpressionWrapper, OuterRef, Subquery
from django.db.models.fields import FloatField, DecimalField
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.admin.views.decorators import staff_member_required
from django.db.models import Sum, F, Value
from django.db.models.functions import Coalesce
from .forms import *
from decimal import Decimal
# Create your views here.


def index(request):
    content = Telling.objects.filter(leider__actief='True').values('leider__naam', 'leider__id').order_by('leider').\
        annotate(prijsNormaal=Coalesce(Sum(F('aantalNormaal') * F('prijsKlasse__normaal')), Decimal(0))).\
        annotate(prijsZwaar=Coalesce(Sum(F('aantalZwaar') * F('prijsKlasse__zwaar')), Decimal(0))).\
        annotate(totaal=Coalesce(F('prijsNormaal') + F('prijsZwaar'), Decimal(0))).\
        annotate(betaald=Coalesce(Subquery(Betaling.objects.filter(leider=OuterRef('leider_id')).values('leider').annotate(som=Sum('hoeveelheid')).values('som')), Decimal(0))).\
        annotate(schulden=ExpressionWrapper(F('totaal') -
                                            F('betaald'), output_field=DecimalField()))
    return render(request, 'beheer/index.html', {'content': content})


@staff_member_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return HttpResponseRedirect(reverse('index'))
    else:
        form = AuthenticationForm()
    return render(request, 'beheer/login.html', {'form': form})


@staff_member_required
def prijsKlasse_view(request):
    if request.method == 'POST':
        form = PrijsKlasseForm(data=request.POST)
        if form.errors != True:
            form.save()
            return HttpResponseRedirect(reverse('prijsKlasse'))
    else:
        form = PrijsKlasseForm()

    return render(request, 'beheer/prijsklasse.html', {'form': form, 'prijsKlasses': PrijsKlasse.objects.all()})


@staff_member_required
def prijsKlasse_delete(request, prijsKlasse_id):
    try:
        PrijsKlasse.objects.get(pk=prijsKlasse_id).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse('prijsKlasse'))
    return HttpResponseRedirect(reverse('prijsKlasse'))


@staff_member_required
def leider_delete(request, leider_id):
    l = Leider.objects.get(pk=leider_id)
    # l.actief = False
    # l.save()
    l.delete()
    return HttpResponseRedirect(reverse('leidersUpdate'))


@staff_member_required
def telling_view(request):
    if request.method == 'POST':
        form = TellingForm(data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponseRedirect(reverse('tellen'))
    else:
        form = TellingForm

    return render(request, 'beheer/telling.html', {'form': form})


@staff_member_required
def leider_view(request):
    if request.method == 'POST':
        Nieuweform = NewLeiderForm(data=request.POST)
        if Nieuweform.is_valid():
            Nieuweform.save()
            return HttpResponseRedirect(reverse('leiders'))
    else:
        Nieuweform = NewLeiderForm()
    leiders = Leider.objects.filter(actief=True)

    return render(request, 'beheer/leiders.html', {'newForm': Nieuweform, 'leiders': leiders})


@staff_member_required
def leider_volgorde(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        for i in range(len(data)):
            Leider.objects.filter(actief=True).filter(pk=data[i]).update(volgorde=i)
    return HttpResponseRedirect(reverse('leiders'))


@staff_member_required
def betalingView(request):
    betalingen = Betaling.objects.order_by('-datum')[:5]
    if request.method == 'POST':
        form = BetalingForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('betaling'))
    else:
        form = BetalingForm()
    return render(request, 'beheer/betaling.html', {'form': form, 'betalingen': betalingen})


def leider_detail(request, leider_id):
    datums = []
    normaalCum = []
    zwaarCum = []
    balans = []
    l = get_object_or_404(Leider, pk=leider_id)
    betalingen = Betaling.objects.filter(leider=l).order_by('-datum')
    tellingen = Telling.objects.filter(leider=l)
    for i in range(len(tellingen)):
        tellingen[i].totaal = int(tellingen[i].aantalNormaal or 0) * tellingen[i].prijsKlasse.normaal + int(tellingen[i].aantalZwaar or 0) * tellingen[i].prijsKlasse.zwaar
        tellingen[i].aantalNormaal = int(tellingen[i].aantalNormaal or 0)
        tellingen[i].aantalZwaar = int(tellingen[i].aantalZwaar or 0)
        datums.append(tellingen[i].datum.strftime("%d/%m/%Y"))
        if i != 0:
            normaalCum.append(normaalCum[i-1] +
                              int(tellingen[i].aantalNormaal or 0))
            zwaarCum.append(zwaarCum[i-1] + int(tellingen[i].aantalZwaar or 0))
        else:
            normaalCum.append(int(tellingen[i].aantalNormaal or 0))
            zwaarCum.append(int(tellingen[i].aantalZwaar or 0))

    return render(request, 'beheer/leiderOverzicht.html', {"datums": datums, "tellingen": tellingen, "normaalCum": normaalCum, "zwaarCum": zwaarCum, "balans": balans, "betalingen": betalingen})
