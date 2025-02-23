"""Module defines how qr-scanner url is presented"""
import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# Remember to add upkg link to attribution page
# https://www.geeksforgeeks.org/create-a-qr-code-scanner-or-reader-in-html-css-javascript/
# https://unpkg.com/browse/html5-qrcode@2.3.8/
def scanner(request):
    """Function retrieves scanned qr code's content and either redirects successfully back to map"""
    if request.user.is_anonymous:
        messages.error(request, 'You are not logged in')
        return redirect('../login')
    if request.method == 'POST':
        # retrieves data from json in javascript
        data = json.loads(request.body)
        decoded_test = data.get('decoded')
        # checks if url is successfully scanned
        print('Decoded QR Code: ', decoded_test)
        # send to javascript and redirect back to map
        return JsonResponse({'redirect_url': '/map/'})
    return render(request, 'scan.html')
