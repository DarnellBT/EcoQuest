from django.urls import path
from . import views

urlspattern = [
     path('about/', views.about, name='about')
]