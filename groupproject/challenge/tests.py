"""Module contains test cases for challenges"""
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from registration.models import UserProfile

from .models import Challenge, ChallengeCompleted


class ChallengeModelTest(TestCase):
    """Class contains tests that use assert to test challenge models"""

    def test_create_challenge(self):
        """Test creating a Challenge instance"""
        # Creates a user instance.
        challenge = Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        self.assertEqual(challenge.challenge, 'Test challenge name')
        self.assertEqual(challenge.description, 'This is the description of the test challenge.')
        self.assertEqual(challenge.points, 10)
