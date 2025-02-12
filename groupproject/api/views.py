from django.template import loader
from django.http import HttpResponse

def api(response):
    template = loader.get_template('api.html')
    return HttpResponse(template.render())