from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from registration.models import UserProfile
from django.contrib import messages

def leaderboard_page(request):
    if request.method == "GET":
        if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')
        username = request.user.username
      
        id = request.user.id
        
        userprofiles = UserProfile.objects.all()
        userprofiles = list(userprofiles)
        points_list = []
        for profile in userprofiles:
            points = profile.points
            points_list.append(points)
            points_list = sorted(points_list, reverse=True)

      
        rank_list = []
        for point in points_list:
            rank_user = UserProfile.objects.get(points=point)
            rank_user = rank_user.user.username
            rank_list.append(rank_user)

      
        rank = []
        len_username = len(rank_list) + 1
        for i in range(1, len_username):
            rank.append(i)

        
        combined_list = zip(rank, rank_list, points_list)

        context = {
            'combined_list': combined_list,
        }

        return render(request, 'leaderboard.html', context)
     
    