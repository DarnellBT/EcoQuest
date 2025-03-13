from django.contrib import messages
from django.shortcuts import render, redirect
from registration.models import UserProfile


def leaderboard_page(request):
    """Function retrieves all user usernames, points and ranks them"""
    if request.method == "GET":
        
        # retrieves userprofiles 
        userprofiles = UserProfile.objects.all()
        userprofiles = list(userprofiles)
        points_list = []
        # retrieves points and sorts them in descending order
        for profile in userprofiles:
            points = profile.points
            points_list.append(points)  # it retrieves the username by points and the
            points_list = sorted(points_list, reverse=True)
        rank_list = []
        # ranks users according to their points in descending order (puts user.username in ranked)
        ranked = UserProfile.objects.all().order_by('-points', 'user__username')[:5]
        # gets the usernames associated with the points  
        for rank_user in ranked:
            rank_list.append(rank_user.user.username)

        rank = []
        # changes 0 index to 1 index
        len_username = len(rank_list) + 1
        for i in range(1, len_username):
            rank.append(i)
            # combines all lists into easier format
        combined_list = zip(rank, rank_list, points_list)
        context = {
            'combined_list': combined_list,
        }
        return render(request, 'leaderboard.html', context)
