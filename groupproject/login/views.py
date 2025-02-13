from django.template import loader
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def loginPage(request):
    #load default login form
    form = LoginForm()
    # check if user has submitted the form
    if request.method == 'POST':
        #take the data submitted from the form 
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            # check whether there username and password are valid
            user = authenticate(request, username=username, password=password)
            if user is not None:
                #check user table against details provided to validate user
                login(request, user)
                return redirect('../home/')
            else:
                print('Authentication failed')
        else:
            print("Form validation failed")
    return render(request, 'loginPage.html', {'form': form})


        
    

