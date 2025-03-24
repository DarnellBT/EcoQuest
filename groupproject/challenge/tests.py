"""Module contains test cases for challenges"""
import sys
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from registration.models import UserProfile
from .models import Challenge, ChallengeCompleted
from .forms import ImageUpload
from io import BytesIO
from PIL import Image
from django.utils.datastructures import MultiValueDict


def setup_account(instance):
    """Sets up a user account for testing."""
    # Registers user.
    register_form_data = {
        'username': 'Dragonite',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'JohnDoe@email.com',
        'password1': 'secret_pass',
        'password2': 'secret_pass',
        'private_policy': True,
    }
    instance.client.post('/register/', register_form_data)
    form_data = {
        'username': 'JohnDoe@email.com',
        'password': 'secret_pass'
    }
    instance.client.post('/login/', form_data)


def generate_test_image():
    """Generates a test image."""
    # Creates image
    file = BytesIO()
    image = Image.new('RGB', (1000, 1000))
    image.save(file, 'png')
    file.seek(0)
    upload_image = InMemoryUploadedFile(
        file,
        field_name='test',
        name='test.png',
        content_type='image/png',
        size=sys.getsizeof(file),
        charset='utf-8',
    )
    return upload_image


class ChallengeModelTest(TestCase):
    """Class contains tests that use assert to test challenge models"""

    def test_create_challenge(self):
        """Test creating a Challenge instance"""
        # Creates a challenge instance.
        challenge = Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        self.assertEqual(challenge.challengeId, 1, 'The challengeId should be 1 for the first challenge created.')
        self.assertEqual(challenge.challenge, 'Test challenge name', 'The challenge name was not correctly stored.')
        self.assertEqual(challenge.description, 'This is the description of the test challenge.', 'The challenge desciption was not stored or cannot be accessed correctly.')
        self.assertEqual(challenge.points, 10, 'The challenge points was not stored or cannot be accessed correctly.')

    def test_create_challenge_completed(self):
        """Test creating a ChallengeCompleted instance"""
        # Create User instance
        user = User.objects.create(
            username='Dragonite',
            first_name='John',
            last_name='Doe',
            email='JohnDoe@email.com',
        )
        user.set_password('secret_pass')
        # Create UserProfile instance
        user_profile = UserProfile.objects.create(
            user=user,
        )
        # Creates a challenge instance.
        challenge = Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        challenge_completed = ChallengeCompleted.objects.create(
            userId=user_profile,
            challengeId=challenge,
            completed=False,
        )
        # Assertion tests for ChallengeCompleted
        self.assertEqual(challenge_completed.userId.userId, 1, 'The completed challenge was not assigned to the correct user.')
        self.assertEqual(challenge_completed.challengeId.challengeId, 1, 'The challenge was not completed for the correct user.')
        self.assertFalse(challenge_completed.completed, 'The challenge should not be completed.')


class ChallengeViewTest(TestCase):
    """Class tests if pages load"""

    def test_challenge_page_loads(self):
        """Test if the challenge page loads successfully"""
        # Creates a challenge instance.
        Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        # Registers user.
        setup_account(self)
        # Check we successfully load challenge page and we also get the challenge template.
        response = self.client.get(reverse('challenge', kwargs={'id': 1}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'challenge.html')

    def test_map_page_redirect_loads(self):
        """Test if the map page loads successfully"""
        # Create Challenge instance
        Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        # Registers user.
        setup_account(self)
        form_data = {
            'image': [generate_test_image()]
        }
        # Upload image.
        # File named 'test.png' is uploaded to 'groupproject/static/Image/' and should be deleted after testing
        response = self.client.post('/challenge/1/', form_data)
        # Check we successfully redirect to map at we also get the map template.
        map_response = self.assertRedirects(response, '/map/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        self.assertTemplateUsed(map_response, '../map/templates/map.html')
        # Assertion tests for if user profile has been updated
        # user_profile = UserProfile.objects.get(userId=1)
        # self.assertEqual(user_profile.points, 10)

    def test_login_page_redirect_loads_when_logout(self):
        """Test if the login page loads successfully when a user logs out."""
        setup_account(self)
        response = self.client.get(reverse('logout'))
        login_response = self.assertRedirects(response, 'login', status_code=302, target_status_code=404, fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        response = self.client.get(reverse('challenge', kwargs={'id': 1}))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301, fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')


class ImageUploadTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""

    def test_valid_form(self):
        """Test if the form is valid"""
        form_data = {
            'image': [generate_test_image()]
        }
        form = ImageUpload({}, MultiValueDict(form_data))
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        # Uploads invalid empty image.
        form_data = {
            'image': []
        }
        form = ImageUpload({}, MultiValueDict(form_data))
        self.assertFalse(form.is_valid())
        # Uploads invalid empty file.
        form_data = {
            'image': [
                InMemoryUploadedFile(
                    BytesIO(b''),
                    field_name='test',
                    name='test.png',
                    content_type='image/png',
                    size=0,
                    charset='utf-8',
                )
            ]
        }
        form = ImageUpload({}, MultiValueDict(form_data))
        self.assertFalse(form.is_valid())
        # Uploads invalid file type.
        file = BytesIO()
        image = Image.new('RGB', (1000, 1000))
        image.save(file, 'png')
        file.seek(0)
        form_data = {
            'image': [
                InMemoryUploadedFile(
                    file,
                    field_name='test',
                    name='test.txt',
                    content_type='text/plain',
                    size=sys.getsizeof(file),
                    charset='utf-8',
                )
            ]
        }
        form = ImageUpload({}, MultiValueDict(form_data))
        self.assertFalse(form.is_valid())
