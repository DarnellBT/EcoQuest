from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegistrationForm
from .models import UserProfile

def register(request):
    form = RegistrationForm()
    #for developers to know fields in a form, allow them to edit
    '''for d in form.fields:
        print('field name:', d)
        print('field label:', form.fields[d].label)
        print('field text:', form.fields[d].help_text)
        print("")'''
    

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            try:
                user = form.save()
        
                return redirect('../login/')
            except:
                return render(request, 'registration.html', {'form':form})
        else:
            
            x = form.fields['username']
          
            x.help_text = "Please enter only Letters, Digits, and @ /./+/-/_"
            y = form.fields['password2']
            y.help_text = "Please enter the same password as before."
            z = form.fields['email']
            z.help_text = "Email is already taken"
        
            return render(request, 'registration.html', {'form':form})
    else:
        form = RegistrationForm()
        x = form.fields['username']
        x.help_text = "Please enter only Letters, Digits, and @ /./+/-/_"
        y = form.fields['password2']
        y.help_text = "Please enter the same password as before."
    return render(request, 'registration.html', {'form':form})

