from . import views
from django.urls import path

urlpatterns = {
    path('admin-portal/', views.admin_portal, name='admin-portal'),
    path('admin-portal/edit-location/', views.admin_location, name='admin-location'),
    path('admin-portal/edit-quiz/', views.admin_quiz, name='admin-quiz'),
    path('admin-portal/edit-question/', views.admin_question, name='admin-question'),
    path('admin-portal/edit-challenge/', views.admin_challenge, name='admin-challenge'),
    path('gamekeeper-portal/', views.gamekeeper_portal, name="gamekeeper-portal"),
    path('admin-portal/edit-location/edit-location/<int:location_id>/', views.edit_location, name='edit_location'),
    path('admin-portal/edit-location/delete-location/<int:location_id>/', views.delete_location, name='delete_location'),
    path('admin-portal/edit-quiz/edit-quiz/<int:quiz_id>/', views.edit_quiz, name='edit_quiz'),
    path('admin-portal/edit-quiz/delete-quiz/<int:quiz_id>/', views.delete_quiz, name='delete_quiz'),
    path('admin-portal/edit-question/edit-question/<int:question_id>/', views.edit_question, name='edit_question'),
    path('admin-portal/edit-question/delete-question/<int:question_id>/', views.delete_question, name='delete_question'),
    path('admin-portal/edit-challenge/edit-challenge/<int:challenge_id>/', views.edit_challenge, name='edit_challenge'),
    path('admin-portal/edit-challenge/delete-challenge/<int:challenge_id>/', views.delete_challenge, name='delete_challenge'),
}

