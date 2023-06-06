from django.contrib import admin
from django.urls import path


from . import views

urlpatterns = [
    path('print/<int:bestellung>', views.generate_pdf, name="generate_pdf"),
]