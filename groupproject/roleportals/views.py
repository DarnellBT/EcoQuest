from django.shortcuts import render, redirect
from challenge.models import Challenge, ChallengeCompleted, ChallengeImages
from django.contrib.auth.models import User
from registration.models import UserProfile

def admin_portal(request):
    return render(request, 'admin_page.html')

def gamekeeper_portal(request):
    all_entries = ChallengeImages.objects.all()
    all_info = []

    if len(all_entries) > 0:
        for entry in all_entries:
            info = []
            info.append(entry.user.id)
            info.append(entry.challenge.challenge)
            info.append(entry.image.url)
            info.append(entry.challenge.points)
            info.append(entry.imageId)
        all_info.append(info)

        if request.method == 'POST':
            userId = request.POST.get("userId")
            challenge_info = request.POST.get("challenge")
            rejected = request.POST.get(f"rejected_{userId}_{challenge_info}")
            approved = request.POST.get(f"approved_{userId}_{challenge_info}")
            imageId = request.POST.get("imageId")
    
            if approved:
                challenge = Challenge.objects.get(challenge=challenge_info)
                user_profile = UserProfile.objects.get(userId=userId)
                ChallengeCompleted.objects.create(userId=user_profile, challengeId=challenge, completed=True)
                ChallengeImages.objects.filter(imageId=imageId).delete()
                challenge_points = challenge.points
                user_profile.points += challenge_points
                user_profile.save()

                return redirect("./")
            if rejected:
                return redirect("./")

        context = {
        'info':all_info,
        }
        return render(request, "game_keeper.html", context)
    else:
        return render(request, "game_keeper.html")




    


    

   



#imageId = models.BigAutoField(primary_key=True, null=False)
#user = models.ForeignKey(User, on_delete=models.CASCADE)
#challenge = models.ForeignKey('Challenge', on_delete=models.CASCADE)
#image = models.ImageField(upload_to='./static/Image/')



#Functionality needed
# Create, Modify, Delete Database Records
# UserProfile
# Quiz
# Question
# Challenge
# Location