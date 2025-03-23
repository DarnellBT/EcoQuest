from django.contrib import messages
from django.core.files.storage import default_storage
from django.shortcuts import redirect, render
from registration import models as register_models

from .forms import ImageUpload
from .models import Challenge, ChallengeCompleted, ChallengeImages


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
    user_obj = register_models.UserProfile.objects.get(userId=request.user.id)
    challenge_completed_obj = ChallengeCompleted.objects.filter(challengeId=challenge_obj, userId=user_obj)
    # if the record exists, user is redirected to map as they have already completed it
    if challenge_completed_obj.exists() == True:
        messages.error(request, "You have already completed this challenge")
        return redirect("../../../map/")
    else: 
        pass

    all_challenge = Challenge.objects.filter(challengeId=id)
    form = ImageUpload()
    # retrieve fields from Challenge objects
    for challenge in all_challenge:
        challenge_task = challenge.challenge
        challenge_description = challenge.description
        challenge_points = challenge.points

    # retrieve current user and their id
    current_user = request.user
    current_user_id = current_user.id

    user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
    user_points = user_profile.points
    context = {
        'user_id': current_user.id,
        'challenge_points': challenge_points,
        'user_points': user_points,
        'forms': form,
        'challenge_descr': challenge_description,
        'challenge': challenge_task,
        'id': id,
    }

    if request.method == 'POST':
        # retrieve data from form and file
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image")
            # create new records in database for image 
            ChallengeImages.objects.create(user=user_profile.user,challenge=Challenge.objects.get(challengeId=id), image=img)
            
            user_profile = register_models.UserProfile.objects.get(userId=current_user_id)

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
