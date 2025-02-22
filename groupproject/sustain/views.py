from django.shortcuts import render, redirect
from django.contrib import messages

def sustain(request):
    if request.user.is_anonymous:
            messages.error(request, 'You are not logged in')
            return redirect('../login')
    return render(request, 'sustain.html')