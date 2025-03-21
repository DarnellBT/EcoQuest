"""Module defines homepage paths"""
from django.shortcuts import render
from django.contrib.auth.models import User
from registration.models import UserProfile

# Function retrieves the home page if user is logged in
def home(request):
    """
    Handles the home page view.
    Displays the homepage with user-specific data if authenticated.
    """
    if request.method == "GET":

        if request.user.is_anonymous:
            userprofile = None
        else:
            userprofile = UserProfile.objects.get(userId=request.user.id)


        return render(request, 'home.html', {'userprofile':userprofile, 'user_auth':request.user})

def privacy(request):
    """
    Handles the privacy policy page view.
    Displays the privacy policy with user-specific data if authenticated.
    """
    if request.method == 'GET':
        if request.user.is_anonymous:
            userprofile = None
        else:
            userprofile = UserProfile.objects.get(userId=request.user.id)
        
        return render(request, 'privacy.html', {'userprofile':userprofile, 'user_auth':request.user})