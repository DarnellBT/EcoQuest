from . import views
from django.urls import path

urlpatterns = [
    path('sustainability', views.sustain, name='sustainability')
]