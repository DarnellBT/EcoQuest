"""Module defines homepage paths"""
from django.shortcuts import render, redirect
from django.contrib import messages
from registration.models import UserProfile

# Function retrieves the home page if user is logged in
def home(request):
    """Function defines homepage logic"""
    if request.method == "GET":
        return render(request, 'home.html')


                
       
    
    
    
