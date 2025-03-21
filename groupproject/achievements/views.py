from django.shortcuts import render
from registration.models import UserProfile
from challenge.models import Challenge, ChallengeCompleted

def achievements(request):


    if request.user.is_anonymous:
        userprofile = None
    else:
        userprofile = UserProfile.objects.get(user=request.user)

    """
    Handles the achievements page.
    Displays a list of challenges and indicates whether each challenge has been completed by the user.
    """

    if request.method == "GET":

        userprofile = UserProfile.objects.get(userId=request.user.id)
        challenges = Challenge.objects.all()
        print(userprofile)
        print(challenges)

        challenges_list = []
        

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

        context = {
            'challenges_list': challenges_list,

            }

        return render(request, "achievements.html", context)
