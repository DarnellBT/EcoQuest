from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def dashboard(request):
    return render(request, 'dashboard.html')

def edit(request):
    return render(request, 'dashboard_edit.html')


def challenges(request):
    return render(request, 'dashboard_challenges.html')


def statistics(request):
    return render(request, 'dashboard_statistics.html')