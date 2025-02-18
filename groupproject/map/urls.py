from django.urls import path
from .views import MapView, submit_location

urlpatterns = [
    path('', MapView.as_view(), name='map'),
    path('submit-location/', submit_location, name='submit_location'),
]