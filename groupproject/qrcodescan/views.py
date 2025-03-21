"""Module defines how qr-scanner url is presented"""
import json
from registration.models import UserProfile
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import redirect
from django.shortcuts import render


# Remember to add upkg link to attribution page
# https://www.geeksforgeeks.org/create-a-qr-code-scanner-or-reader-in-html-css-javascript/
# https://unpkg.com/browse/html5-qrcode@2.3.8/
def scanner(request):
    """
    Handles the QR code scanner page.
    Retrieves scanned QR code content and redirects the user based on the decoded data.
    """
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    
    userprofile = UserProfile.objects.get(user=request.user)
    if request.method == 'POST':
        # retrieves data from json in javascript
        data = json.loads(request.body)
        decoded_test = data.get('decoded')
        # checks if url is successfully scanned
        
        # send to javascript and redirect back to map
        return JsonResponse({'redirect_url': f'../{decoded_test}/'})
    return render(request, 'scan.html', {'user_auth': request.user, 'userprofile':userprofile})
