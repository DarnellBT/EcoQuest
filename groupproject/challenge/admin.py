from django.contrib import admin

from .models import ChallengeCompleted, Challenge, ChallengeImages


class ChallengeProfile(admin.ModelAdmin):
    list_display = ['challengeId', 'challenge', 'description', 'points']


class CompletedProfile(admin.ModelAdmin):
    list_display = ['userId', 'challengeId', 'completed']

class ChallengeImagesProfile(admin.ModelAdmin):
    list_display = ['imageId', 'user', 'challenge', 'image']


admin.site.register(Challenge, ChallengeProfile)
admin.site.register(ChallengeCompleted, CompletedProfile)
admin.site.register(ChallengeImages, ChallengeImagesProfile)