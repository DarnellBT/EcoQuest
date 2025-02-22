from django.shortcuts import redirect, render
from .models import Challenge
from .models import ChallengeCompleted
from .forms import ImageUpload
from django.core.files.storage import default_storage
from registration import models as register_models
from django.contrib import messages

def challenge(request, id):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../../login')
    all_challenge = Challenge.objects.filter(challengeId=id)
    form = ImageUpload()
    # retrieve fields from Challenge objects
    for challenge in all_challenge:
        challenge_task = challenge.challenge
        challenge_description = challenge.description
        challenge_points = challenge.points

    upload_status = 'Upload Successful'
    current_user = request.user
    current_user_id = current_user.id
    
    user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
    user_points = user_profile.points
    context = {
        'user_id': current_user.id,
        'challenge_points': challenge_points,
        'user_points': user_points,
        'forms':form,
        'challenge_descr': challenge_description,
        'challenge': challenge_task,
        'id': id,
    }

    if request.method == 'POST':
        # retrieve data from form and file
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            # retrieve image and path to img (where it will be saved)
            img = form.cleaned_data.get("image")
            img_path = f'./challenge/static/Image/{img}'
            # use form data and save the image
            with default_storage.open(img_path, 'wb+') as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            upload_status = 'Upload Successful'
            current_user = request.user
            current_user_id = current_user.id
            user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
            # Add points for challenge
            user_points = user_profile.points + challenge_points
            user_profile.points = user_points
            # save new points and create a record in ChallengeCompleted
            user_profile.save()
            ChallengeCompleted.objects.create(userId=user_profile, challengeId=challenge, completed=True)
            context = {
                'user_id': current_user.id,
                'user_points': user_points,
                'image': img,
                'upload_status': upload_status,
                'challenge_descr': challenge_description,
                'challenge': challenge_task,
                'id': id,
                }
            return redirect('../../map/')
    return render(request, 'challenge.html', context)