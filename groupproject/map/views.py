from django.views.generic import TemplateView
import folium
from django.db import models
import folium.plugins
import folium.plugins.locate_control
from folium.plugins import LocateControl
from django.http import HttpResponse
from ipware import get_client_ip
from django.shortcuts import redirect
from .models import Location



class MapView(TemplateView):
    template_name = 'map.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Create a map figure, with inial location and settings
        mapFig = folium.Map(
            location=[50.73632605587163, -3.5348055751142917],
            zoom_start=14,
            tiles='OpenStreetMap',
            width=800,
            height=800,
            
        )

        folium.plugins.LocateControl(auto_start=True).add_to(mapFig)
      
        # Create marker with popup and hover text
        all_locations = Location.objects.all()
        all_list = list(all_locations)
        for data in all_list:
            folium.Marker(
                location=[data.latitude, data.longitude],
                popup=f'{data.name}',
                tooltip=f'Test{data.locationId}'
            ).add_to(mapFig)

      
        # render map to html format
        map_html = mapFig._repr_html_()

        # pass html content to map.html
        context['map'] = map_html
        
        #send it to map
        return context


