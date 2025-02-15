from django.shortcuts import render
import random
from .models import Challenge
from .models import ChallengeCompleted

def challenge(request):
    totalChallenges = Challenge.objects.all().count()
    challenge_num = random.randint(1,totalChallenges)
    return render(request, 'challenge.html', {'total':challenge_num})