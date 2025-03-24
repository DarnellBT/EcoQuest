"""Module defined what admin can see in admin portal"""
from django.contrib import admin

from .models import Question, Quiz, QuizCompleted


# pylint: disable=line-too-long

class QuizAdmin(admin.ModelAdmin):
    """Defined attributes from table, admin can see"""
    list_display = ['quizId', 'name']


class QuestionAdmin(admin.ModelAdmin):
    """Defined attributes from table, admin can see"""
    list_display = ['questionId', 'quiz', 'question', 'choice1', 'choice2', 'choice3', 'choice4', 'answer', 'points']

class QuizCompletedAdmin(admin.ModelAdmin):
    list_display = ['user', 'quiz', 'completed']

admin.site.register(Quiz, QuizAdmin)
admin.site.register(QuizCompleted, QuizCompletedAdmin)
admin.site.register(Question, QuestionAdmin)
