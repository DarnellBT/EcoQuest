from django.template import loader
from django.http import HttpResponse
from registration.models import UserProfile
from django.shortcuts import render, redirect
from django.contrib import messages

# Function retrieves the home page if user is logged in
def home(request):
  
    if request.method == "GET":
        # checks if user is not logged in
        if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')

        # gets current user object from db
        current_user = UserProfile.objects.get(user=request.user)
        # checks if user is assigned role user and renders homepage [auto-assigned on registration]
        if current_user.is_user:
            return render(request, 'home.html')
                
       
    
    
    
