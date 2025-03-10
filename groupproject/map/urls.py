from django.urls import path
from qrcodescan import views as qr_view
import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('map/submit-location/', views.submit_location, name='submit_location'),
    path('../qr-scanner/', qr_view.scanner, name='qr-scanner'),
]
