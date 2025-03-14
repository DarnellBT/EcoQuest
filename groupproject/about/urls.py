"""Setup paths for about views."""
from django.urls import path

from . import views

urlspattern = [
    path('contact/', views.contact, name='contact')
]
