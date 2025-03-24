"""Module defined django models to create tables in database"""
from django.db import models
from django.contrib.auth.models import User

class Quiz(models.Model):
    """Attributes in Quiz table"""
    quizId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Question(models.Model):
    """Attributes in Question table"""
    questionId = models.BigAutoField(primary_key=True)
    #quizId = models.IntegerField(default=0)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question = models.CharField(max_length=300)
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    points = models.IntegerField(default=0)

    def __str__(self):
        return self.question

class QuizCompleted(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    quiz = models.ForeignKey(Quiz, on_delete=models.DO_NOTHING)
    completed = models.BooleanField()
