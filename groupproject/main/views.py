from django.template import loader
from django.http import HttpResponse

def home(response):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())