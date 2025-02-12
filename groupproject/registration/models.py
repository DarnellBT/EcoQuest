from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    userId = models.BigAutoField(primary_key=True),
    points = models.IntegerField(max_length=10, default=0),
    is_user = models.BooleanField(default=1),
    is_developer = models.BooleanField(default=0),
    is_admin = models.BooleanField(default=0)   