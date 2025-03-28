from django.shortcuts import render, redirect
from django.contrib import messages
from registration import models as register_models
from .models import Challenge, ChallengeCompleted, ChallengeImages
from .forms import ImageUpload

def challenge(request, id):
    """
    Handles the challenge page.
    Displays challenge details and allows users to upload images as proof of completion.
    Prevents users from reattempting completed challenges.
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../../login')
    
    # retrieve records from the database
    challenge_obj = Challenge.objects.get(challengeId=id)
    
    # Get the user profile and check if the user has completed the challenge already
    user_obj = register_models.UserProfile.objects.get(userId=request.user.id)
    challenge_completed_obj = ChallengeCompleted.objects.filter(challengeId=challenge_obj, userId=user_obj)
    # if the record exists, user is redirected to map as they have already completed it
    if challenge_completed_obj.exists() == True:
        messages.error(request, "You have already completed this challenge")
        return redirect("../../../map/")

    # Get challenge details
    challenge_task = challenge_obj.challenge
    challenge_description = challenge_obj.description
    challenge_points = challenge_obj.points

    # Initialize form for image upload
    form = ImageUpload()

    # retrieve current user and their id
    current_user = request.user
    current_user_id = current_user.id

    user_points = user_obj.points
    context = {
        'user_id': request.user.id,
        'challenge_points': challenge_points,
        'user_points': user_points,
        'forms': form,
        'challenge_descr': challenge_description,
        'challenge': challenge_task,
        'id': id,
        'userprofile': user_obj,  # Pass user profile data to the template
        'user_auth': request.user,  # Pass the user object to the template
    }

    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image")
            # create new records in database for 
     
            ChallengeImages.objects.create(user=user_obj.user,challenge=Challenge.objects.get(challengeId=id), image=img)
            
            user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
            user_points = user_profile.points
            context = {
                'user_id': current_user.id,
                'user_points': user_points,
                'image': img,
                'challenge_descr': challenge_description,
                'challenge': challenge_task,
                'id': id,
            }
            return redirect('../../map/')

    return render(request, 'challenge.html', context)
