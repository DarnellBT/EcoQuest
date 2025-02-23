"""
Module Handles register/ page 
"""
from django.shortcuts import render, redirect
from .forms import RegistrationForm

def register(request):
    """
    Function puts a form into html with various fields given text. 
    Saves user details if valid
    """
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                # save user
                form.save()
                return redirect('../login/')
            except Exception as e:
                print(f"{"Exception: ", str(e)}")
                return render(request, 'registration.html', {'form':form})
        else:
            x = form.fields['username']
            x.help_text = "<br/>Please enter only Letters, Digits, and @ /./+/-/_"
            y = form.fields['password2']
            y.help_text = ""
            z = form.fields['email']
            z.help_text = "Email is already taken"
            return render(request, 'registration.html', {'form':form})
    else:
        # Defines form fields with help messages assigned to them
        form = RegistrationForm()
        x = form.fields['username']
        x.help_text = "<br/>Please enter only Letters, Digits, and @ /./+/-/_"
        y = form.fields['password2']
        y.help_text = ""
    return render(request, 'registration.html', {'form':form})
