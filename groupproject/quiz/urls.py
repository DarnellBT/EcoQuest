"""Module defined connection between view and url"""
from django.urls import path
from . import views

urlpatterns = [
    path('quiz/<int:id>/', views.quiz, name='quiz'),
]
