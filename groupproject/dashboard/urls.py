from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/edit/', views.edit, name='edit'),
    path('dashboard/challenges/', views.challenges, name='challenges'),
    path('dashboard/statistics/', views.statistics, name='statistics')
]