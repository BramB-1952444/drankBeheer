from django.db import models
from django.db.models.expressions import OrderBy

class Leider(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    volgorde = models.IntegerField(default=500, blank=True)
    actief = models.BooleanField(default=True, blank=False)

    def __str__(self):
        return self.naam
    
    class Meta:
        ordering = ['volgorde']

class PrijsKlasse(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    normaal = models.DecimalField(max_digits=6, decimal_places=2)
    zwaar = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.naam + " - €" + str(self.normaal) + " - €" + str(self.zwaar)

class Telling(models.Model):
    leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    aantalNormaal = models.IntegerField(default=0, null=True)
    aantalZwaar = models.IntegerField(default=0, null=True)
    prijsKlasse = models.ForeignKey(PrijsKlasse, on_delete=models.PROTECT)
    datum = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self):
        return str(self.leider) + ' normaal:' + str(self.aantalNormaal) + ' zwaar:' + str(self.aantalZwaar)

    class Meta:
        verbose_name_plural = "Tellingen"

class Betaling(models.Model):
    leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    hoeveelheid = models.DecimalField(max_digits=8, decimal_places=2)
    datum = models.DateTimeField(auto_now_add=True, blank=True)
    def __str__(self) -> str:
        return str(self.leider) + " - " + str(self.hoeveelheid)

    class Meta:
        verbose_name_plural = "Betalingen"