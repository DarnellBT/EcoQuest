from challenge.models import Challenge, ChallengeCompleted
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth import logout
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from registration.models import UserProfile
from .forms import UserForm

def dashboard(request):
    """
    Handles the account page.
    Displays user-specific information and allows account deletion.
    """
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
        'user_auth': request.user,
        'userprofile': current_user_object,
        'username': username,
        'firstName': first_name,
        'lastName': last_name,
        'email': email,
        'points': points,
        'role': role,
        'userId':current_user_id,
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



def logout_dashboard(request):
    """
    Logs out the user and redirects them to the homepage.
    """
    # removes session and takes user to login page
    logout(request)
    return redirect("../../../")

def edit_account(request):
    """
    Handles editing user account details.
    Updates user information if the form is valid.
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    # retrieve object or raise exception if not found
    userprofile = get_object_or_404(UserProfile, userId=request.user.id)
    user_instance = userprofile.user
    if request.method == "POST":
        form = UserForm(request.POST, instance=user_instance)
        if form.is_valid():
            # save updated info
            form.save()
            return redirect('../')
    else: 
        #pass in current info
        form = UserForm(instance=user_instance)
    return render(request, 'edit_details.html', {'form': form})

def rewards(request):
    """
    Displays the rewards page.
    Shows the user's progress towards earning rewards based on their points.
    """
    if request.method == 'GET':

        if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')

        userprofile = get_object_or_404(UserProfile, userId=request.user.id)
        user_points = userprofile.points
      
        rewards = [['Bronze', 100, "cross.png"], ['Silver', 250, "cross.png"], ['Gold', 500, "cross.png"]]
        user_rewards = []
        if user_points >= rewards[0][1]:
            rewards[0][2] = "tick.png"
            user_rewards.append(rewards[0])
        else:
            user_rewards.append(rewards[0])
        
        if user_points >= rewards[1][1]:
            rewards[1][2] = "tick.png"
            user_rewards.append(rewards[1])
        else:
            user_rewards.append(rewards[1])

        if user_points >= rewards[2][1]:
            rewards[2][2] = "tick.png"
            user_rewards.append(rewards[2])
        else:
            user_rewards.append(rewards[2])



        context = {
            'rewards': user_rewards,
        }
        print(user_rewards)
    return render(request, 'rewards.html', context)

