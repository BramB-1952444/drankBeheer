from django import forms
from django.db.models.base import Model
from django.forms import ModelForm, fields
from django.forms.formsets import ORDERING_FIELD_NAME
from django.forms.models import model_to_dict
from .models import Leider, PrijsKlasse, Telling, Betaling

class PrijsKlasseForm(ModelForm):
    class Meta:
        model = PrijsKlasse
        fields = ['naam', 'normaal', 'zwaar']

class TellingForm(forms.Form):
    prijsKlasse = forms.ModelChoiceField(queryset=PrijsKlasse.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        leiders = Leider.objects.all()
        for leider in leiders:
            self.fields['normaal_%s' % (leider)] = forms.IntegerField(required=False, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
            self.fields['normaal_%s' % (leider)].group = leider
            self.fields['zwaar_%s' % (leider)] = forms.IntegerField(required=False, min_value=0, widget=forms.TextInput(attrs={'class': 'form-control'}))
            self.fields['zwaar_%s' % (leider)].group = leider
    
    def save(self):
        data = self.cleaned_data
        for leider in Leider.objects.all():
            t = Telling(prijsKlasse=data['prijsKlasse'], leider=leider, aantalNormaal=data['normaal_%s' % (leider)], aantalZwaar=data['zwaar_%s' % (leider)])
            t.save()

class BetalingForm(ModelForm):
    class Meta:
        model = Betaling
        fields = ['leider', 'hoeveelheid']

class NewLeiderForm(ModelForm):
    class Meta:
        model = Leider
        fields = ['naam']

class LeiderVolgordeForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        leiders = Leider.objects.all()
        for leider in leiders:
            self.fields[str(leider)] = forms.IntegerField(required=True, widget=forms.TextInput({'class': 'form-control', 'value' : leider.volgorde}))
    
    def save(self):
        data = self.cleaned_data
        for leider in Leider.objects.all():
            leider.volgorde = data[str(leider)]
            leider.save()
