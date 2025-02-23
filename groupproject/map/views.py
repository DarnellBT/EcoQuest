"""Module contains logic for map page"""
import base64
import json
import folium
import folium.elements
import folium.plugins
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from django.http import JsonResponse
from quiz import models as quiz_model
from challenge.models import Challenge, ChallengeCompleted
from registration.models import UserProfile
from .models import Location
# pylint: disable = line-too-long

class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Create a map figure, with initial location and settings
        mapFig = folium.Map(
            location=[50.73632605587163, -3.5348055751142917],
            zoom_start=7,
            tiles='OpenStreetMap',
            width="100%",
            height="100%",
        )
        
        folium.plugins.LocateControl(auto_start=True).add_to(map_fig)
        # Create markers with popup and hover text
        all_locations = Location.objects.all()
        for data in all_locations:
            print(f"Adding marker for location: {data.name}, Latitude: {data.latitude}, Longitude: {data.longitude}")
            file = f"./{data.qr_code.url[1:]}"
            # convert to a renderable image in popup
            encoded = base64.b64encode(open(file, 'rb').read())
            svg = ("""<object data="data:image/png;base64,{}" width="{}" height="{}" type="image/svg+xml">
            </object>""").format
            width, height, fat_wh = 230, 230, 1.4
            iframe = folium.IFrame(svg(encoded.decode('UTF-8'), width, height), width=width*fat_wh, height=height*fat_wh)
            popup = folium.Popup(iframe, max_width=300)
            folium.Marker(
                location=[data.latitude, data.longitude],
                popup=popup,
                tooltip=f'Test{data.locationId}'
            ).add_to(map_fig)
        # Add a specific marker at given coordinates
        specific_lat = 50.7350
        specific_lon = -3.5343
        folium.Marker(
            location=[specific_lat, specific_lon],
            popup='Specific Location',
            tooltip='Specific Marker'
        ).add_to(map_fig)
        # Render map to HTML format
        map_html = map_fig._repr_html_()
        # Pass HTML content to map.html
        context['map'] = map_html
        #send it to map
        return context

def submit_process(request):
    """Function processes POST method once form is submitted"""
    if request.method == 'POST':    
        # retrieve form data and get all Location and Challenge objects    
        randomString = request.POST.get('randomString')
        all_locate = Location.objects.all()
        list_locate = list(all_locate)
        all_challenges = Challenge.objects.all()
        challenges_list = list(all_challenges)
        current_user_id = request.user.id
        current_user_object = UserProfile.objects.get(userId=current_user_id)
        # Get all challenges completed by user 
        all_completed = ChallengeCompleted.objects.filter(userId=current_user_object).values_list("challengeId", flat=True)
        incomplete_challenges = [challenge for challenge in challenges_list if challenge.challengeId not in all_completed]
        challenge_ids = []
        for incomplete in incomplete_challenges:
            challenge_ids.append(incomplete.challengeId)
        validated_string = ""
        # Check for each location
        for locate in list_locate:
            # retrieve the text inside qr code from Location table
            qr_message = locate.qr_code_message
            if randomString == qr_message:
                validated_string = "QR Code Valid"
                challenge_id = locate.challengeId
                # If challenge_id is 0 then redirect to random quiz and if not then go to specific challenge
                if challenge_id != 0 and (challenge_id in challenge_ids):
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
    """Handles POST method from javascript (geolocation of user)"""
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')
        # Process the latitude and longitude as needed
        print(f"Received location: Latitude: {latitude}, Longitude: {longitude}")
        return JsonResponse({'status': 'success', 'latitude': latitude, 'longitude': longitude})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)


