import base64
import random
import folium
import folium.elements
import folium.plugins
from django.views.generic import TemplateView
from django.shortcuts import redirect, render
from .models import Location
from .forms import StringForm


class MapView(TemplateView):
    template_name = 'map.html'
    forms = StringForm()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Create a map figure, with inial location and settings
        mapFig = folium.Map(
            location=[50.73632605587163, -3.5348055751142917],
            zoom_start=7,
            tiles='OpenStreetMap',
            width=800,
            height=800,
            
        )

        folium.plugins.LocateControl(auto_start=True).add_to(mapFig)
     
       
        file = "./map/static/Hello.png"
        encoded = base64.b64encode(open(file, 'rb').read())
        svg = ("""<object data="data:image/png;base64,{}" width="{}" height="{} type="image/svg+xml">
    </object>""").format
        width, height, fat_wh = 170, 170, 1.4
        iframe = folium.IFrame(svg(encoded.decode('UTF-8'), width, height), width=width*fat_wh, height=height*fat_wh)
        popup = folium.Popup(iframe, max_width=400)
        
        # Create marker with popup and hover text
        all_locations = Location.objects.all()
        all_list = list(all_locations)
        for data in all_list:
            folium.Marker(
                location=[data.latitude, data.longitude],
                popup=popup,                      #f'{data.name}',
                tooltip=f'Test{data.locationId}'
            ).add_to(mapFig)

        
        # render map to html format
        map_html = mapFig._repr_html_()
        
        # pass html content to map.html
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
                
                
            else:
                validated_string = "QR Code Invalid"
                
        return render(request, 'submitProcessing.html', {'valid_or_invalid':validated_string})
    return render(request, 'submitProcessing.html')