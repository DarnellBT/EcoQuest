import base64
import json
import random
from django.http import JsonResponse
import folium
import folium.elements
import folium.plugins
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .models import Location
from .forms import StringForm
from quiz import models as quiz_model
from django.contrib import messages
from challenge import models as challenge_model
from django.http import JsonResponse
import json

class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Create a map figure, with initial location and settings
        mapFig = folium.Map(
            location=[50.73632605587163, -3.5348055751142917],
            zoom_start=7,
            tiles='OpenStreetMap',
            width=800,
            height=800,
        )

        folium.plugins.LocateControl(auto_start=True).add_to(mapFig)
        
        # Create markers with popup and hover text
        all_locations = Location.objects.all()
        for data in all_locations:
            print(f"Adding marker for location: {data.name}, Latitude: {data.latitude}, Longitude: {data.longitude}")
            file = "./map/" + data.qr_code.url[1:]
            while file.count('/map/map') > 0:
                file = file.replace('/map/map/', '/map/')
            encoded = base64.b64encode(open(file, 'rb').read())
            svg = ("""<object data="data:image/png;base64,{}" width="{}" height="{}" type="image/svg+xml">
            </object>""").format
            width, height, fat_wh = 170, 170, 1.4
            iframe = folium.IFrame(svg(encoded.decode('UTF-8'), width, height), width=width*fat_wh, height=height*fat_wh)
            popup = folium.Popup(iframe, max_width=400)
            folium.Marker(
                location=[data.latitude, data.longitude],
                popup=popup,
                tooltip=f'Test{data.locationId}'
            ).add_to(mapFig)

        # Add a specific marker at given coordinates
        specific_lat = 50.7350
        specific_lon = -3.5343
        folium.Marker(
            location=[specific_lat, specific_lon],
            popup='Specific Location',
            tooltip='Specific Marker'
        ).add_to(mapFig)

        # Render map to HTML format
        map_html = mapFig._repr_html_()
        
        # Pass HTML content to map.html
        context['map'] = map_html
        

        #send it to map
        return context



def submitProcess(request):
    if request.method == 'POST':        
        randomString = request.POST.get('randomString')
        all_locate = Location.objects.all()
        list_locate = list(all_locate)
        validated_string = ""
        for locate in list_locate:
            qr_message = locate.qr_code_message
            if randomString == qr_message:
                validated_string = "QR Code Valid"
                challenge_id = locate.challengeId
                if challenge_id != 0:
                    return redirect(f'../../challenge/{challenge_id}/')
              
                else:
                    random_quiz = quiz_model.Quiz.objects.order_by('?').first()
                    quiz_id = random_quiz.quizId
                    return redirect(f'../../quiz/{quiz_id}/')
            else:
                validated_string = "QR Code Invalid"
                
        return render(request, 'submitProcessing.html', {'valid_or_invalid':validated_string})
    return render(request, 'submitProcessing.html')


def submit_location(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        # Process the latitude and longitude as needed
        print(f"Received location: Latitude: {latitude}, Longitude: {longitude}")
        return JsonResponse({'status': 'success', 'latitude': latitude, 'longitude': longitude})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)
