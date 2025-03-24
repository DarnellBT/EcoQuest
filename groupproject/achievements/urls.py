from django.urls import path
from . import views

urlspattern = [
    path('achievements/', views.achievement, name='achievements')
]
