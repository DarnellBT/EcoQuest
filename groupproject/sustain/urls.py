"""
Module defines the url path for the sustainability webpage
"""
from django.urls import path
from . import views


#links url path and view
urlpatterns = [
    path('sustainability', views.sustain, name='sustainability')
]
