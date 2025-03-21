from django.contrib import messages
from django.shortcuts import render, redirect
from registration.models import UserProfile

def leaderboard_page(request):
    """Function retrieves all user usernames, points and ranks them"""
    if request.method == "GET":
        
        # Retrieve all user profiles
        userprofiles = UserProfile.objects.all().order_by('-points', 'user__username')
        
        # Create a ranking system
        rank_list = []
        prev_points = None
        rank = 0
        
        for index, profile in enumerate(userprofiles):
            if profile.points != prev_points:
                rank = index + 1  # New rank if different points
            prev_points = profile.points
            rank_list.append((rank, profile.user.username, profile.points))
        
        # Extract top 5 users
        top_5 = rank_list[:5]

        # Check if the user is logged in
        user_rank = None
        current_user_points = None
        user_entry = None
        userprofile = None  # Ensure `userprofile` is available

        if request.user.is_authenticated:
            # Get the logged-in user's profile
            userprofile = UserProfile.objects.get(user=request.user)
            current_user_points = userprofile.points
            
            # Check if user is in top 5
            user_entry = next((entry for entry in rank_list if entry[1] == request.user.username), None)
            
            if user_entry:
                user_rank = user_entry[0]
            
            # If the user isn't in the top 5, show them separately at the bottom
            if user_rank and user_rank > 5:
                user_entry = (user_rank, request.user.username, current_user_points)
            else:
                user_entry = None  # Don't show duplicate if already in top 5

        context = {
            'combined_list': top_5,
            'user_entry': user_entry,  # Holds current user info if not in top 5
            'user_auth': request.user,
            'userprofile': userprofile,  # Pass userprofile to template
        }

        return render(request, 'leaderboard.html', context)
