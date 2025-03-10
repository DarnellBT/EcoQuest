from django.urls import path
from qrcodescan import views as qr_view
import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('../qr-scanner/', qr_view.scanner, name='qr-scanner'),
]
