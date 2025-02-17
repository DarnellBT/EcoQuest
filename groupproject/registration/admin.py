from django.contrib import admin
from .models import UserProfile
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('userId', 'username', 'first_name', 'last_name', 'email','password', 'points', 'is_user', 'is_game_keeper', 'is_admin')
    
    def username(self, obj):
        return obj.user.username

    def first_name(self, obj):
        return obj.user.first_name

    def last_name(self, obj):
        return obj.user.last_name

    def email(self, obj):
        return obj.user.email
    
    def password(self,obj):
        return obj.user.password


admin.site.register(UserProfile, UserProfileAdmin)

