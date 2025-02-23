"""
Module handles connection between url and views
"""
from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register')
]
