from django import forms
from map.models import Location
from challenge.models import Challenge
from quiz.models import Quiz, Question

class LocationForm(forms.ModelForm):
    class Meta:
        model = Location
        fields = ['name', 'latitude', 'longitude', 'icon']

class ChallengeForm(forms.ModelForm):
    class Meta:
        model = Challenge
        fields = ['challenge', 'description', 'points']

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['name']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['quiz', 'question', 'choice1', 'choice2', 'choice3', 'choice4', 'answer', 'points']