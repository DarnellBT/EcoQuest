from django.contrib import admin

from .models import ChallengeCompleted, Challenge


class ChallengeProfile(admin.ModelAdmin):
    list_display = ['challengeId', 'challenge', 'description', 'points']


class CompletedProfile(admin.ModelAdmin):
    list_display = ['userId', 'challengeId', 'completed']


admin.site.register(Challenge, ChallengeProfile)
admin.site.register(ChallengeCompleted, CompletedProfile)
