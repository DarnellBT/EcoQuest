from django.template import loader
from django.http import HttpResponse

def login(response):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())