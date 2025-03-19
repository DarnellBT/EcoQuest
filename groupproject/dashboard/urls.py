from django.urls import path

from . import views

urlpatterns = [
    path('account/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_dashboard, name="logout"),
    path('account/edit-account/', views.edit_account, name='edit_account'),
    path('account/rewards/', views.rewards, name='rewards')
]
