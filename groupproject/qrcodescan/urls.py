from . import views
from django.urls import path

urlpatterns = [
    path('qr-scanner/', views.scanner, name='scanner')
]