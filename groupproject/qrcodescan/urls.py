"""Module handles connection between url and view logic"""
from django.urls import path
from . import views

urlpatterns = [
    path('qr-scanner/', views.scanner, name='scanner')
]
