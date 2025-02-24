from challenge.models import Challenge, ChallengeCompleted
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from registration.models import UserProfile

from .forms import NameForm, UsernameForm, PasswordForm


def dashboard(request):
    """Handles account page - not yet renamed to account"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    # retrieves current user object data by user id
    current_user_id = request.user.id
    current_user_object = UserProfile.objects.get(userId=current_user_id)
    username = current_user_object.user.username
    first_name = current_user_object.user.first_name
    last_name = current_user_object.user.last_name
    email = current_user_object.user.email
    points = current_user_object.points
    # checks which role user is and assigns role a string
    if current_user_object.is_admin:
        role = 'Admin'
    elif current_user_object.is_game_keeper:
        role = 'Game Keeper'
    else:
        role = 'User'
    # prepares to send data to html
    context = {
        'username': username,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'points': points,
        'role': role,
    }
    # only runs if a form is submitted (delete account in this case)
    if request.method == "POST":
        current_userprofile = UserProfile.objects.get(userId=request.user.id)
        current_user = User.objects.get(username=username)
        # deletes both User and UserProfile from database
        current_user.delete()
        current_userprofile.delete()
        return redirect("../../register")
    return render(request, 'dashboard.html', context)


def challenges(request):
    """Function handles account challenge pages"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # retrieves all challenges
    all_challenges = Challenge.objects.all()
    challenges_list = list(all_challenges)
    current_user_id = request.user.id
    current_user_object = UserProfile.objects.get(userId=current_user_id)
    # Retrives all completed challenges done by user
    all_completed = ChallengeCompleted.objects.filter(userId=current_user_object).values_list("challengeId", flat=True)
    # Fill with incompleted challenges, check and put any challenges not in completed
    incomplete_challenges = [challenge for challenge in challenges_list if challenge.challengeId not in all_completed]
    return render(request, 'dashboard_challenges.html', {'challenges': incomplete_challenges})


def change_uname(request):
    """
    Function to provide render html page and process username updating
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    # initialise form
    form = UsernameForm()
    if request.method == "POST":
        # retrieve data from form
        username = request.POST.get('username')
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        # get User object from UserProfile object
        for current_user in current_user_list:
            current_user_object = current_user.user
        current_user_object.username = username
        current_user_object.save()
    return render(request, 'dashboard_username.html', {'form': form})


def change_name(request):
    """
    Function to provide render html page and process name updating
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    form = NameForm()
    if request.method == "POST":
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.filter(userId=current_user_id)
        current_user_list = list(current_user_object)
        for current_user in current_user_list:
            current_user_object = current_user.user
        current_user_object.first_name = first_name
        current_user_object.last_name = last_name
        current_user_object.save()
    return render(request, 'dashboard_name.html', {'form': form})


def change_password(request):
    """
    Function to provide render html page and process password updating
    """
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
        # uses django set_password function to replace password (adds salting, hashing etc)
        current_user_object.set_password(password)
        current_user_object.save()
        # updates cookie so user isn't logged out and can carry on
        update_session_auth_hash(request, current_user_object)
        return redirect('change-password')
    return render(request, 'dashboard_password.html', {'form': form})


def logout_dashboard(request):
    # removes session and takes user to login page
    logout(request)
    return redirect("../../login")
