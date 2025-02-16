from django.shortcuts import render
import random
from .models import Challenge
from .models import ChallengeCompleted

def challenge(request, id):
    totalChallenges = Challenge.objects.all().count()
    if totalChallenges == 0:
        challenge_num = 0
    elif totalChallenges > 1:
        challenge_num = random.randint(1,totalChallenges)
    else: 
        challenge_num = 1
    return render(request, 'challenge.html', {'total':challenge_num}, {'id': id})