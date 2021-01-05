from django.db import models

class Leider(models.Model):
    naam = models.CharField(max_length=100, unique=True)
    volgorde = models.IntegerField()

    def __str__(self):
        return self.naam

class PrijsKlasse(models.Model):
    naam = models.CharField(max_length=50, unique=True)
    normaal = models.DecimalField(max_digits=6, decimal_places=2)
    zwaar = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.naam + " - €" + str(self.normaal) + " - €" + str(self.zwaar)
    
class Telling(models.Model):
    leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    aantalNormaal = models.IntegerField(default=0)
    aantalZwaar = models.IntegerField(default=0)
    prijsKlasse = models.ForeignKey(PrijsKlasse, on_delete=models.PROTECT)

class Betaling(models.Model):
    leider = models.ForeignKey(Leider, on_delete=models.CASCADE)
    hoeveelheid = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self) -> str:
        return str(self.Leider) + " - " + str(self.hoeveelheid)