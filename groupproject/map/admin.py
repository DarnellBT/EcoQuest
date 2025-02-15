from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ['locationId', 'name', 'latitude', 'longitude', 'qr_code', 'qr_code_message', 'task']

admin.site.register(Location, LocationAdmin)