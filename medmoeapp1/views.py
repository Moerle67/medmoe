from django.shortcuts import render
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
width, height = A4
# Create your views here.

def index(request):
    # Create a file-like buffer to receive PDF data.
    buffer = io.BytesIO()

    # Create the PDF object, using the buffer as its "file."
    p = canvas.Canvas(buffer, pagesize=A4)
    p._fontsize=12

    # Draw things on the PDF. Here's where the PDF generation happens.
    # See the ReportLab documentation for the full list of functionality.
    p.drawString(10*mm, height-20*mm, "Hello world.")
    for zeile in range(10):
        p.drawString(10*mm,height-20*mm-(zeile+1)*12, f"Zeile gg {zeile}")

    # Close the PDF object cleanly, and we're done.
    p.showPage()
    p.save()

    # FileResponse sets the Content-Disposition header so that browsers
    # present the option to save the file.
    buffer.seek(0)
    print(A4)
    return FileResponse(buffer, as_attachment=True, filename="hello.pdf")