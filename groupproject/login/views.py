from django.template import loader
from django.shortcuts import render
from django.http import HttpResponse, request
from django.contrib.auth import authenticate
from . import forms

def loginPage(response):
    template = loader.get_template('loginPage.html')
    return HttpResponse(template.render())

