from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .forms import *
from registration.models import UserProfile
from challenge.models import Challenge, ChallengeCompleted
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages

def dashboard(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')
    current_user_id = request.user.id
   
    current_user_object = UserProfile.objects.get(userId=current_user_id)
   
    username = current_user_object.user.username
    firstName = current_user_object.user.first_name
    lastName = current_user_object.user.last_name
    email = current_user_object.user.email
    points = current_user_object.points

    if current_user_object.is_admin:
        role = 'Admin'
    elif current_user_object.is_game_keeper:
        role = 'Game Keeper'
    else:
        role = 'User'

    context = {
        'username':username,
        'firstName':firstName,
        'lastName':lastName,
        'email':email,
        'points':points,
        'role':role,
    }

    if request.method == "POST":
        current_userprofile = UserProfile.objects.get(userId=request.user.id)
        current_user = User.objects.get(username=username)
        current_user.delete()
        current_userprofile.delete()
        

        return redirect("../../register")

    return render(request, 'dashboard.html', context)

def challenges(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../../login')
    all_challenges = Challenge.objects.all()
    challenges_list = list(all_challenges)
    current_user_id = request.user.id

    current_user_object = UserProfile.objects.get(userId=current_user_id)
    
    all_completed = ChallengeCompleted.objects.filter(userId=current_user_object).values_list("challengeId", flat=True)
    incomplete_challenges = [challenge for challenge in challenges_list if challenge.challengeId not in all_completed]
    
    return render(request, 'dashboard_challenges.html', {'challenges':incomplete_challenges})


def change_uname(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../../login')
    form = UsernameForm()
    if request.method == "POST":
        username = request.POST.get('username')
        
        current_user_id = request.user.id
        
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user

        current_user_object.username = username
        current_user_object.save()
    return render(request, 'dashboard_username.html', {'form':form})

def change_name(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../../login')
    form = NameForm()
    if request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('lastName')
        current_user_id = request.user.id
        
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user

        current_user_object.first_name = firstName
        current_user_object.last_name = lastName
        current_user_object.save()
    return render(request, 'dashboard_name.html', {'form':form})

def change_password(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../../login')
    form = PasswordForm()
    if request.method == "POST":
        password = request.POST.get('password')
        current_user_id = request.user.id
        
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user
            

        
        current_user_object.set_password(password)
        current_user_object.save()
        update_session_auth_hash(request, current_user_object)
        return redirect('change-password')
    return render(request, 'dashboard_password.html', {'form':form})

def logout_dashboard(request):
    logout(request)
    return redirect("../../login")