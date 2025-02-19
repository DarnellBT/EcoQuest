from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/challenges/', views.challenges, name='challenges'),
    path('dashboard/change-username/', views.change_uname, name='change-uname'),
    path('dashboard/change-name/', views.change_name, name='change-name'),
    path('dashboard/change-password/', views.change_password, name='change-password'),
    path('logout/', views.logout_dashboard, name="logout")

]