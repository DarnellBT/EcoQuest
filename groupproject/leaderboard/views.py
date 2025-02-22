from django.shortcuts import render, redirect
from registration.models import UserProfile
from django.contrib import messages

def leaderboard_page(request):
    """Function retrieves all user usernames, points and ranks them"""
    if request.method == "GET":
        if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')
        # retrieves userprofiles
        userprofiles = UserProfile.objects.all()
        userprofiles = list(userprofiles)
        points_list = []
        # retrieves points and sorts them in descending order
        for profile in userprofiles:
            points = profile.points
            points_list.append(points)
            points_list = sorted(points_list, reverse=True)
        rank_list = []
        # ranks users according to their points
        for point in points_list:
            rank_user = UserProfile.objects.get(points=point)
            rank_user = rank_user.user.username
            rank_list.append(rank_user)
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
     
    