"""Module contains logic for map page"""
import folium
import folium.plugins
from django.contrib.messages import get_messages
from django.templatetags.static import static
from django.views.generic import TemplateView
from .models import Location
from registration.models import UserProfile


class MapView(TemplateView):
    """
    Handles the map page view.
    Displays a map with markers for all locations and user-specific data if authenticated.
    """
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
         
            icon_url =f'static/images/{data.icon}.png'  # Generate full static URL

            folium.Marker(
                location=[data.latitude, data.longitude],
                icon=folium.CustomIcon(
                    icon_image=icon_url,  # Use absolute URL for icon
                    icon_size=(30, 30)  # Ensure correct display size
                ),
                tooltip=f'{data.name}',
                popup=f"<strong>{data.name}</strong>"
            ).add_to(map_fig)

        # Render map to HTML format
        context['map'] = map_fig._repr_html_()
        context['user_auth'] = self.request.user
        context['userprofile'] = userprofile  # Pass user profile to template
        
        return context