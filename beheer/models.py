from django.db import models
from django.db.models.deletion import PROTECT

class Leider(models.Model):
    naam = models.CharField(max_length=100)
    volgorde = models.IntegerField()

    def __str__(self):
        return self.naam

class PrijsKlasse(models.Model):
    naam = models.CharField(max_length=50)
    normaal = models.DecimalField(max_digits=6, decimal_places=2)
    zwaar = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.naam

class Telling(models.Model):
    leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    aantalNormaal = models.IntegerField()
    aantalZwaar = models.IntegerField()
    prijsKlasse = models.ForeignKey(PrijsKlasse, on_delete=models.PROTECT)

class Betaling(models.Model):
    Leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    hoeveelheid = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self) -> str:
        return str(self.Leider) + " - " + str(self.hoeveelheid)