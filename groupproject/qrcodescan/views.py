import json
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
# Remember to add upkg link to attribution page
# https://www.geeksforgeeks.org/create-a-qr-code-scanner-or-reader-in-html-css-javascript/
# https://unpkg.com/browse/html5-qrcode@2.3.8/
def scanner(request):

    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')
    
    if request.method == 'POST':
        data = json.loads(request.body)
        decoded_test = data.get('decoded')
        print('Decoded QR Code: ', decoded_test)
        
        
        return JsonResponse({'redirect_url': '/map/'})

    return render(request, 'scan.html')
