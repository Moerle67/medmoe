from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from .models import *
import locale

from datetime import datetime

# Create your views here.

def generate_pdf(request, bestellung):
    width, height = A4
    kante_links = 25*mm
    locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

    # Create a file-like buffer to receive PDF data.
    print(bestellung)
    ds = Bestellung.objects.get(pk=bestellung)
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."

    p = canvas.Canvas(buffer, pagesize=A4)
    
    # Absender linksoben
    p.setFontSize(11)
    p.drawString(kante_links, height-18*mm, ds.kunde.zeile1)
    p.drawString(kante_links, height-22*mm, ds.kunde.zeile2)
    p.drawString(kante_links, height-26*mm, ds.kunde.zeile3)
    
    # Linie
    p.line(kante_links, height-30*mm, 187*mm, height-30*mm)

    # Absender Adressfeld
    p.setFontSize(8)
    p.drawString(kante_links, height-55*mm, f"{ds.kunde.zeile1}, {ds.kunde.zeile2}, {ds.kunde.zeile3}")
    # Linie
    p.line(kante_links, height-57*mm, 100*mm, height-57*mm)

    # Adresse Ziel
    p.setFontSize(11)
    p.drawString(kante_links, height-66*mm, ds.arzt.zeile1)
    p.drawString(kante_links, height-71*mm, ds.arzt.zeile2)
    p.drawString(kante_links, height-76*mm, ds.arzt.zeile3)
    p.drawString(kante_links, height-81*mm, ds.arzt.zeile4)
    p.drawString(kante_links, height-86*mm, ds.arzt.zeile5)

    # Adresse Kunde
    p.setFontSize(10)
    p.drawString(134*mm, height-53*mm, ds.kunde.zeile1)
    p.drawString(134*mm, height-58*mm, ds.kunde.zeile2)
    p.drawString(134*mm, height-63*mm, ds.kunde.zeile3)
    p.drawString(134*mm, height-68*mm, ds.kunde.email)
    p.drawString(134*mm, height-73*mm, ds.kunde.telefon)

    p.drawString(134*mm, height-106*mm, ds.bestell_datum.strftime("%d. %B %Y"))

    p.setFontSize(25)

    ds_med = ds.medikamente.all()
    ds_ueber = ds.ueberweisung.all()

    word_rezept = ""
    word_ueber = ""
    word_binde = ""

    if len(ds_med)==1:
        word_rezept = "Rezept"
    elif len(ds_med)>1:
            word_rezept = "Rezepte"
    else:
         word_rezept = ""   

    if len(ds_ueber)==1:
        word_ueber = "Überweisung"
    elif len(ds_ueber)>1:
        word_ueber = "Überweisungen"
    else:
         word_ueber = ""

    if len(ds_med)>0 and len(ds_ueber)>0:
         word_binde = " und "

    p.drawString(kante_links, height-120*mm, f"{word_rezept}{word_binde}{word_ueber}")
    
    zeile = 0
    start = 135
    step = 8
    p.setFontSize(11)

    ds_med = ds.medikamente.all()
    if len(ds_med) > 0: 
        p.drawString(kante_links, height-(start+zeile*step)*mm, "Sehr geehrte Damen und Herren,")
        zeile += 1
        p.drawString(kante_links, height-(start+zeile*step)*mm, "hiermit bitte ich Sie um Rezepte für folgende notwendige Medikamente:")
        zeile += 1
        for medikament in ds_med:
            p.drawString(kante_links+5, height-(start+zeile*step)*mm, f"- {medikament.details}")
            zeile += 1
            
    zeile+=1
    

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
   
    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename=f"Bestellung_{ds.bezeichnung}_{ds.bestell_datum}.pdf")