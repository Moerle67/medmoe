from django.db import models

# Create your models here.

class Kontakt(models.Model):
    name = models.CharField("Name", max_length=50)
    zeile1 = models.CharField("1. Adresszeile (Name)", max_length=50, primary_key=True)
    zeile2 = models.CharField("2. Adresszeile (Straße)", max_length=50)
    zeile3 = models.CharField("3. Adresszeile (PLZ Ort)", max_length=50)
    zeile4 = models.CharField("4. Adresszeile", max_length=50, blank=True)
    zeile5 = models.CharField("5. Adresszeile", max_length=50, blank=True)
    zeile6 = models.CharField("6. Adresszeile", max_length=50, blank=True)
    email = models.CharField("E-Mail", max_length=50, blank=True)
    telefon = models.CharField("E-Telefon", max_length=50, blank=True)
    
    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakts"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kontakt_detail", kwargs={"pk": self.pk})

class Medikament(models.Model):
    bezeichnung = models.CharField("Bezeichnung", max_length=50)
    details = models.CharField("Details", max_length=100)
    menge = models.IntegerField("Menge in Packung")
    einnahme = models.IntegerField("Regelmäßige Einnahme (Tag)")
    letze_bestellung = models.DateField("Letzte Bestellung", auto_now=False, auto_now_add=True)
    letzte_lieferung = models.DateField("Letzte Lieferung", auto_now=False, auto_now_add=False, blank=True)

    class Meta:
        verbose_name = "Medikament"
        verbose_name_plural = "Medikamente"

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Medikament_detail", kwargs={"pk": self.pk})
