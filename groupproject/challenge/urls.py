from django.urls import path

from . import views

urlspattern = [
    path('challenge/<int:id>/', views.challenge, name='challenge')
]
