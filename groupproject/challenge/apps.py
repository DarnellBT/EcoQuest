"""Setup table for challenge models."""
from django.apps import AppConfig


class ChallengeConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'challenge'
