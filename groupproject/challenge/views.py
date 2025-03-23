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

    # Get the challenge object by its id
    challenge_obj = Challenge.objects.get(challengeId=id)
    
    # Get the user profile and check if the user has completed the challenge already
    user_obj = register_models.UserProfile.objects.get(userId=request.user.id)
    challenge_completed_obj = ChallengeCompleted.objects.filter(challengeId=challenge_obj, userId=user_obj)

    if challenge_completed_obj.exists():
        messages.error(request, "You have already completed this challenge")
        return redirect("../../../map/")

    # Get challenge details
    challenge_task = challenge_obj.challenge
    challenge_description = challenge_obj.description
    challenge_points = challenge_obj.points

    # Initialize form for image upload
    form = ImageUpload()

    # Get the user's current points
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
            ChallengeImages.objects.create(user=user_obj.user, challenge=challenge_obj, image=img)
            upload_status = 'Upload Successful'

            # Add the challenge completion record
            ChallengeCompleted.objects.create(userId=user_obj, challengeId=challenge_obj, completed=True)

            context.update({
                'upload_status': upload_status,
                'image': img,
            })
            return redirect('../../map/')

    return render(request, 'challenge.html', context)
