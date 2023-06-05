from django.db import models

# Create your models here.

class Kontakt(models.Model):
    name = models.CharField(verbose_name="Name", max_length=50)
    zeile1 = models.CharField(verbose_name="1. Adresszeile (Name)", max_length=50, primary_key=True)
    zeile2 = models.CharField(verbose_name="2. Adresszeile (Straße)", max_length=50)
    zeile3 = models.CharField(verbose_name="3. Adresszeile (PLZ Ort)", max_length=50)
    zeile4 = models.CharField(verbose_name="4. Adresszeile", max_length=50, blank=True)
    zeile5 = models.CharField(verbose_name="5. Adresszeile", max_length=50, blank=True)
    zeile6 = models.CharField(verbose_name="6. Adresszeile", max_length=50, blank=True)
    email = models.CharField(verbose_name="E-Mail", max_length=50, blank=True)
    telefon = models.CharField(verbose_name="E-Telefon", max_length=50, blank=True)
    
    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakte"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Kontakt_detail", kwargs={"pk": self.pk})

class Medikament(models.Model):
    bezeichnung = models.CharField(verbose_name="Bezeichnung", max_length=50)
    details = models.CharField(verbose_name="Details", max_length=100)
    beschreibung = models.TextField(verbose_name="Beschreibung", blank=True)
    menge = models.IntegerField(verbose_name="Menge in Packung")
    einnahme = models.IntegerField(verbose_name="Regelmäßige Einnahme (Tag)")
    letze_bestellung = models.DateField(verbose_name="Letzte Bestellung", auto_now=False, auto_now_add=True)

    class Meta:
        verbose_name = "Medikament"
        verbose_name_plural = "Medikamente"

    def __str__(self):
        return f"{self.bezeichnung} - {self.beschreibung}"

    def get_absolute_url(self):
        return reverse("Medikament_detail", kwargs={"pk": self.pk})

class Ueberweisung(models.Model):
    bezeichnung = models.CharField(verbose_name="Bezeichnung", max_length=50)
    details = models.CharField(verbose_name="Details", max_length=100)
    termin = models.DateTimeField(verbose_name="Termin", auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = "Ueberweisung"
        verbose_name_plural = "Ueberweisungen"

    def __str__(self):
        return f"{self.bezeichnung} ({self.termin})"

    def get_absolute_url(self):
        return reverse("Ueberweisung_detail", kwargs={"pk": self.pk})


class Bestellung(models.Model):
    bezeichnung = models.CharField(verbose_name="Bezeichnung", max_length=50)
    bestell_datum = models.DateField(verbose_name="Bestelldatum", auto_now=False, auto_now_add=True)
    kunde = models.ForeignKey(Kontakt, verbose_name="Kunde", on_delete=models.RESTRICT, related_name="Kunde")
    arzt = models.ForeignKey(Kontakt, verbose_name="Arzt", on_delete=models.RESTRICT, related_name="Arzt")
    bemerkung = models.TextField("Bemerkung", blank=True)
    medikamente = models.ManyToManyField(Medikament, verbose_name="Medikamente", blank=True)
    ueberweisung = models.ManyToManyField(Ueberweisung, verbose_name="Überweisungen", blank=True)
    
    class Meta:
        verbose_name = "Bestellung"
        verbose_name_plural = "Bestellungen"
        ordering = ['-bestell_datum']

    def __str__(self):
        return f"{self.bezeichnung} - {self.arzt} ({self.bestell_datum})"

    def get_absolute_url(self):
        return reverse("Bestellungdetail", kwargs={"pk": self.pk})

