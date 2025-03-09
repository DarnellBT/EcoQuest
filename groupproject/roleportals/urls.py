from . import views
from django.urls import path

urlpatterns = {
    path('admin-portal/', views.admin_portal, name='admin-portal'),
    path('gamekeeper-portal/', views.gamekeeper_portal, name="gamekeeper-portal"),
}

