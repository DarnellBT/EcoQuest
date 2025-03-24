"""Registering model with admin portal."""
from django.contrib import admin

from .models import UserProfile


class UserProfileAdmin(admin.ModelAdmin):
    """Class  tells admin portal what attributes of database should be shown"""
    list_display = (
    'userId', 'username', 'first_name', 'last_name', 'email', 'password', 'points', 'is_user', 'is_game_keeper',
    'is_admin')

    def username(self, obj):
        """Retrieves username from user within UserProfile object"""
        return obj.user.username

    def first_name(self, obj):
        """Retrieves firstName from user within UserProfile object"""
        return obj.user.first_name

    def last_name(self, obj):
        """Retrieves lastName from user within UserProfile object"""
        return obj.user.last_name

    def email(self, obj):
        """Retrieves email from user within UserProfile object"""
        return obj.user.email

    def password(self, obj):
        """Retrieves password from user within UserProfile object"""
        return obj.user.password


admin.site.register(UserProfile, UserProfileAdmin)
