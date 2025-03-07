"""Module defined django models to create tables in database"""
from django.db import models


class Quiz(models.Model):
    """Attributes in Quiz table"""
    quizId = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=50)


class Question(models.Model):
    """Attributes in Question table"""
    questionId = models.BigAutoField(primary_key=True)
    quizId = models.IntegerField(default=0)
    question = models.CharField(max_length=300, default='NULL')
    choice1 = models.CharField(max_length=200)
    choice2 = models.CharField(max_length=200)
    choice3 = models.CharField(max_length=200)
    choice4 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    points = models.IntegerField(default=0)
