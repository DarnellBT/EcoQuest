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

    def test_create_challenge_completed(self):
        """Test creating a ChallengeCompleted instance"""
        # Create Challenge instance
        challenge = Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        # Registers user
        register_form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        }
        self.client.post('/register/', register_form_data)
        # Logs user in
        login_form_data = {
            'username': 'Dragonite',
            'password': 'secret_pass'
        }
        self.client.post('/login/', login_form_data)
        # Uploads image
        with open('./challenge/static/Image/Test.png', 'rb') as image:
            form_data = {
                'image': SimpleUploadedFile(name='Test.png', content=image.read(), content_type='image/png')
            }
            self.client.post('/challenge/1/', form_data)
        challenge_completed = ChallengeCompleted.objects.get(challengeId=1)
        user_profile = UserProfile.objects.get(userId=1)
        # Assertion tests for ChallengeCompleted
        self.assertEqual(challenge_completed.userId, user_profile)
        self.assertEqual(challenge_completed.challengeId, challenge)
        self.assertEqual(challenge_completed.completed, True)
        # Assertion tests for if user profile has been updated
        self.assertEqual(user_profile.points, 10)


class ChallengeViewTest(TestCase):
    """Class tests if pages load"""

    def test_challenge_page_loads(self):
        """Test if the challenge page loads successfully"""
        # Create Challenge instance
        Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        # Registers user
        register_form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        }
        self.client.post('/register/', register_form_data)
        # Logs user in
        login_form_data = {
            'username': 'Dragonite',
            'password': 'secret_pass'
        }
        self.client.post('/login/', login_form_data)
        response = self.client.get(reverse('challenge', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'challenge.html')

    
