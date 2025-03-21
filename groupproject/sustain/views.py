"""
Module contains the view for the sustainability page
"""
from django.shortcuts import render

# This file is currently empty. If this app requires views in the future, 
# they should be defined here. Views are responsible for handling HTTP requests 
# and returning HTTP responses, typically by rendering templates or redirecting users.

def sustain(request):
    """Function that retrieves sustain.html"""
    return render(request, 'sustain.html')
