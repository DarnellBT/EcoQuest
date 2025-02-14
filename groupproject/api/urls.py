from django.urls import path
from . import views

urlpatterns = [
    path('admin_api/', views.api, name='api')
]