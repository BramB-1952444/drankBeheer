from django.db.models.deletion import ProtectedError
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .forms import *
# Create your views here.


def index(request):
    return render(request, 'beheer/index.html')

@login_required
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

@login_required
def prijsKlasse_view(request):
    if request.method == 'POST':
        form = PrijsKlasseForm(data=request.POST)
        if form.errors != True:
            form.save()
            return HttpResponseRedirect(reverse('prijsKlasse'))
    else:
        form = PrijsKlasseForm()

    return render(request, 'beheer/prijsklasse.html', {'form': form, 'prijsKlasses': PrijsKlasse.objects.all()})

@login_required
def prijsKlasse_delete(request, prijsKlasse_id):
    try:
        PrijsKlasse.objects.get(pk=prijsKlasse_id).delete()
    except ProtectedError:
        return HttpResponseRedirect(reverse('prijsKlasse')) 
    return HttpResponseRedirect(reverse('prijsKlasse'))