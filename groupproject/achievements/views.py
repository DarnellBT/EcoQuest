from django.shortcuts import render, redirect
from django.contrib import messages
from registration.models import UserProfile
from challenge.models import Challenge, ChallengeCompleted

def achievements(request):
    """
    Handles the achievements page.
    Displays a list of challenges and indicates whether each challenge has been completed by the user.
    """

    # check if user is logged in or not
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    else:
        userprofile = UserProfile.objects.get(user=request.user)


    if request.method == "GET":

        userprofile = UserProfile.objects.get(userId=request.user.id)
        challenges = Challenge.objects.all()

        # initialise empty list 
        challenges_list = []
        
        # for each challenge, go through them and assign them an image if present in database
        for challenge in challenges:
            challenge_list = []
            individual_challenge = challenge.challenge
            challenge_list.append(individual_challenge)
            image = ""
            completed_obj = ChallengeCompleted.objects.filter(userId=userprofile, challengeId=challenge).exists()
           
            if completed_obj:
                image = "tick.png"
                challenge_list.append(image)
            else: 
                image = "cross.png"
                challenge_list.append(image)
            
            
            challenges_list.append(challenge_list)


            context = {
                'challenges_list': challenges_list,
                'user_auth': request.user,  # Pass user authentication status
                'userprofile': userprofile,  # Pass user profile
            }
            

        return render(request, "achievements.html", context)
        


