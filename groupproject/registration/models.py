from django.db import models
from django.contrib.auth.models import User
    
class UserProfile(models.Model):
    userId = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)
    is_user = models.BooleanField(default=1)
    is_developer = models.BooleanField(default=0)
    is_admin = models.BooleanField(default=0)  
    
