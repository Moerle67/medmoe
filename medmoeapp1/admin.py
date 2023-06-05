from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Kontakt)
admin.site.register(Medikament)
admin.site.register(Bestellung)
admin.site.register(Ueberweisung)
