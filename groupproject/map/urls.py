from django.urls import path

import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('map/submit-location/', views.submit_location, name='submit_location'),
]
