from django.contrib import admin

from .models import Leider, PrijsKlasse, Telling, Betaling
# Register your models here.
admin.site.register(Leider)
admin.site.register(PrijsKlasse)
admin.site.register(Telling)
admin.site.register(Betaling)
