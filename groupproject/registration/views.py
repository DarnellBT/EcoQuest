from django.template import loader
from django.http import HttpResponse

def register(response):
    template = loader.get_template('registration.html')
    return HttpResponse(template.render())