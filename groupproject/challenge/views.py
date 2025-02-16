from django.shortcuts import render
import random
from .models import Challenge
from .models import ChallengeCompleted

def challenge(request, id):
    
    context = {
        'id': id,
    }
    return render(request, 'challenge.html', context)