from django.contrib import admin
from .models import Location

class LocationAdmin(admin.ModelAdmin):
    list_display = ('name', 'latitude', 'longitude', 'qr_code', 'qr_code_message', 'challengeId', 'locationId')

admin.site.register(Location, LocationAdmin)