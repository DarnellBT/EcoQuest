"""Module contains test cases for challenges"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import Challenge, ChallengeCompleted
from .forms import ImageUpload
from registration.models import UserProfile


class RegistrationModelTest(TestCase):
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

    def test_create_challenge_completed(self):
        """Test creating a ChallengeCompleted instance"""
        # Creates a challenge instance.
        challenge = Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )

        # Creates a user instance.
        user = User.objects.create(
            username='Dragonite',
            first_name='John',
            last_name='Doe',
            email='JohnDoe@email.com',
        )
        user.set_password('secret_pass')
        # Creates a UserProfile instance
        user_profile = UserProfile.objects.create(user=user, )

#        challenge_completed = ChallengeCompleted.objects.create(
#            userId=user_profile,
#            challengeId=challenge,
#            completed=True
#        )

        form_data = {

        }
        response = self.client.post('/challenge/1/', form_data)
        challenge_completed = ChallengeCompleted.objects.all().first()
        # Assertion tests for ChallengeCompleted
        self.assertEqual(challenge_completed.userId, 1)
        self.assertEqual(challenge_completed.challengeId, 1)
        self.assertEqual(challenge_completed.completed, True)
        # Assertion tests for if user profile has been updated


class ChallengeViewTest(TestCase):
    """Class tests if pages load"""
    def test_challenge_page_loads(self):
        """Test if the registration page loads successfully"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'registration.html')

    def test_map_page_redirect_loads(self):
        """Test if the login page loads successfully"""
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        }

        response = self.client.post('../map/', form_data)
        map_response = self.assertRedirects(response, '../map/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        # Check we get map template.
        self.assertTemplateUsed(map_response, '../map/templates/map.html')
