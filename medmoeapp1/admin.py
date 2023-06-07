from django.contrib import admin
from django.shortcuts import HttpResponseRedirect, redirect


from .models import *
from . import views
# Register your models here.

admin.site.register(Kontakt)
admin.site.register(Ueberweisung)
admin.site.register(Medikament)
# admin.site.register(Termin)
@admin.register(Termin)
class TerminAdmin(admin.ModelAdmin):
    list_filter = ['wer', 'erledigt']


@admin.action(description="PDF generieren")
def pdf_generate(modeladmin, request, queryset):
    for bestellung in queryset:
#        return redirect('generate_pdf', bestellung=bestellung.pk)
        return HttpResponseRedirect(f"/medmoe/print/{bestellung.pk}")


class BestellungAdmin(admin.ModelAdmin):
    actions = [pdf_generate]

admin.site.register(Bestellung, BestellungAdmin)
