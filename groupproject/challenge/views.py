from django.shortcuts import render
import random
from .models import Challenge
from .models import ChallengeCompleted
from .forms import ImageUpload
from django.core.files.storage import default_storage
from registration import models as register_models

def challenge(request, id):
    all_challenge = Challenge.objects.filter(challengeId=id)
    
    form = ImageUpload()
    for challenge in all_challenge:
        challenge_task = challenge.challenge
        challenge_description = challenge.description

    upload_status = 'Upload Successful'
    current_user = request.user
    current_user_id = current_user.id
    
    user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
    user_points = user_profile.points
    context = {
        'user_points': user_points,
        'forms':form,
        'challenge_descr': challenge_description,
        'challenge': challenge_task,
        'id': id,
    }

    if request.method == 'POST':
        form = ImageUpload(request.POST, request.FILES)
        if form.is_valid():
            img = form.cleaned_data.get("image")
            img_path = f'./challenge/static/Image/{img}'
            with default_storage.open(img_path, 'wb+') as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            upload_status = 'Upload Successful'
            current_user = request.user
            current_user_id = current_user.id
    
            user_profile = register_models.UserProfile.objects.get(userId=current_user_id)
            user_points = user_profile.points
            context = {
                'user_points': user_points,
                'image': img,
                'upload_status': upload_status,
                'challenge_descr': challenge_description,
                'challenge': challenge_task,
                'id': id,
                }
            
            
            return render(request, 'challenge.html', context)


    return render(request, 'challenge.html', context)