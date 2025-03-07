"""Module handles connection between settings.py and apps"""
from django.apps import AppConfig


class SustainConfig(AppConfig):
    """makes primary key auto increment for models and gives name to app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sustain'
