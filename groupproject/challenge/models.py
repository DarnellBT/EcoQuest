from django.db import models
from registration.models import UserProfile


class Challenge(models.Model):
    challengeId = models.BigAutoField(primary_key=True, null=False)
    challenge = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)
    points = models.IntegerField(null=False)



class ChallengeCompleted(models.Model):
    userId = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE)
    challengeId = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    completed = models.BooleanField()

