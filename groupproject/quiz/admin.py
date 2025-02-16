from django.contrib import admin
from .models import *

class QuizAdmin(admin.ModelAdmin):
    list_display = ['quizId', 'name']

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['questionId', 'quizId', 'choice1', 'choice2', 'choice3', 'choice4', 'answer', 'points']


admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)