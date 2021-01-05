from django.forms import ModelForm
from .models import Leider, PrijsKlasse, Telling, Betaling
class LeiderForm(ModelForm):
    class Meta:
        model = Leider
        fields = ['naam', 'volgorde']

class PrijsKlasseForm(ModelForm):
    class Meta:
        model = PrijsKlasse
        fields = ['naam', 'normaal', 'zwaar']

class TellingForm(ModelForm):
    class Meta:
        model = Telling
        fields = ['leider', 'aantalNormaal', 'aantalZwaar', 'prijsKlasse']

class BetalingForm(ModelForm):
    class Meta:
        model = Betaling
        fields = ['leider', 'hoeveelheid']