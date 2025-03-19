"""Module contains logic for map page"""
import base64
import json
import math
import folium
import folium.elements
import folium.plugins
from django.contrib.messages import get_messages
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from .models import Location
from registration.models import UserProfile


class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        storage = get_messages(self.request)
        context['messages'] = storage
        storage.used

        # Create a map figure, with initial location and settings
        map_fig = folium.Map(
            location=[50.73632605587163, -3.5348055751142917],
            zoom_start=7,
            tiles='OpenStreetMap',
            width="100%",
            height="100%",
        )

        folium.plugins.LocateControl(auto_start=True).add_to(map_fig)
        
        # Check if user is authenticated
        userprofile = None
        if self.request.user.is_authenticated:
            userprofile = UserProfile.objects.get(user=self.request.user)

        # Create markers with popup and hover text
        all_locations = Location.objects.all()
        for data in all_locations:
            folium.Marker(
                location=[data.latitude, data.longitude],
                icon=folium.CustomIcon(icon_image=f"static/images/{data.icon}.png"),
                tooltip=f'{data.name}',
            ).add_to(map_fig)
        
        # Render map to HTML format
        map_html = map_fig._repr_html_()
        context['map'] = map_html
        context['user_auth'] = self.request.user
        context['userprofile'] = userprofile  # Pass user profile to template
        
        return context


"""
def submit_process(request):
    Function processes POST method once form is submitted
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
        all_completed = ChallengeCompleted.objects.filter(userId=current_user_object).values_list("challengeId",
                                                                                                  flat=True)
        incomplete_challenges = [challenge for challenge in challenges_list if
                                 challenge.challengeId not in all_completed]
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
        return render(request, 'submitProcessing.html', {'valid_or_invalid': validated_string})
    return render(request, 'submitProcessing.html')

def create_map(all_locations):
    Creates a folium map with markers for all locations.
    map_fig = folium.Map(
        location=[50.73632605587163, -3.5348055751142917],
        zoom_start=7,
        tiles='OpenStreetMap',
        width="100%",
        height="100%",
    )

    folium.plugins.LocateControl(auto_start=True).add_to(map_fig)

    specific_lat = 50.7350
    specific_lon = -3.5343
    folium.Marker(
        location=[specific_lat, specific_lon],
        popup='Centre of Campus',
        tooltip='Campus'
    ).add_to(map_fig)

    if len(all_locations) == 0:
        return map_fig._repr_html_()
 

    for data in all_locations:
        folium.Marker(
            location=[data.latitude, data.longitude],
            popup=data.name,
            tooltip=f'{data.name'
        ).add_to(map_fig)

    

    return map_fig._repr_html_()

def submit_location(request):
    Handles POST method from javascript (geolocation of user)
    if request.method == 'POST':
        data = json.loads(request.body)
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        all_locations = Location.objects.all()
        location_include = []
        for location in all_locations:
            loc_lat = location.latitude
            loc_long = location.longitude
            distance = calc_distance(latitude, longitude, loc_lat, loc_long)

            print("Distance to location.name}: ", distance)
            if distance < 40.01:
                location_include.append(location)
        print(f"Locations to include after inclusion: {len(location_include)}")
        print("Locations:", [loc.name for loc in location_include])
        map_html = create_map(location_include)

               

        print(f"Received location: Latitude: {latitude}, Longitude: {longitude}")
        return JsonResponse({'map': map_html})
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=400)

def calc_distance(lat1, lon1, lat2, lon2):

    lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])
    dist_lon = lon2-lon1
    dist_lat = lat2-lat1
    a = math.sin(dist_lat/2)** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dist_lon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    r = 6371000
    return c * r
    """