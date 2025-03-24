from django.db import models
from django.contrib.auth.models import User


class Challenge(models.Model):
    challengeId = models.BigAutoField(primary_key=True, null=False)
    challenge = models.CharField(max_length=200, null=False)
    description = models.CharField(max_length=500, null=False)
    points = models.IntegerField(null=False)

    def __str__(self):
        return self.challenge


class ChallengeCompleted(models.Model):
    userId = models.ForeignKey('registration.UserProfile', on_delete=models.CASCADE)
    challengeId = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    completed = models.BooleanField()

class ChallengeImages(models.Model):
    imageId = models.BigAutoField(primary_key=True, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='./static/Image/')

