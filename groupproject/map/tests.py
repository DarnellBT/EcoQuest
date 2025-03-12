"""Module contains test cases for map"""
from django.test import TestCase
from django.urls import reverse
from .forms import StringForm
from .models import Location
from challenge.models import Challenge
from quiz.models import Quiz, Question


def setup_account(instance):
    """Sets up a user account for testing."""
    # Registers user.
    register_form_data = {
        'username': 'Dragonite',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'JohnDoe@email.com',
        'password1': 'secret_pass',
        'password2': 'secret_pass'
    }
    instance.client.post('/register/', register_form_data)
    form_data = {
        'username': 'JohnDoe@email.com',
        'password': 'secret_pass'
    }
    instance.client.post('/login/', form_data)


class MapModelTest(TestCase):
    """Class contains tests that use assert to test map model"""

    def test_create_location(self):
        """Test creating a Location instance"""
        # Creates a Location instance.
        location = Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='Test.png',
            qr_code_message='mapRandomString',
        )
        self.assertEqual(location.name, 'test_location')
        self.assertEqual(location.latitude, 50.2)
        self.assertEqual(location.longitude, -3.04)
        self.assertEqual(location.qr_code, 'Test.png')
        self.assertEqual(location.qr_code_message, 'mapRandomString')
        self.assertEqual(location.challengeId, 0)


class MapViewTest(TestCase):
    """Class tests if pages load"""

    def test_map_page_loads(self):
        """Test if the map page loads successfully"""
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)
        # Check we get map template.
        self.assertTemplateUsed(response, 'map.html')

    def test_challenge_page_redirect_loads(self):
        """Test if the challenge page loads successfully"""
        # Create Challenge instance.
        Challenge.objects.create(
            challenge='Test challenge name',
            description='This is the description of the test challenge.',
            points=10,
        )
        # Creates a Location instance.
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='test.png',
            qr_code_message='test_message_challenge',
            challengeId=1,
        )
        setup_account(self)
        form_data = {
            'randomString': 'test_message_challenge',
        }
        response = self.client.post('/map/submit/', form_data)
        challenge_response = self.assertRedirects(response, '/challenge/1/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        # Check we get map template.
        self.assertTemplateUsed(challenge_response, '../challenge/templates/challenge.html')

    def test_quiz_page_redirect_loads(self):
        """Test if the quiz page loads successfully"""
        # Creates a quiz instance.
        quiz = Quiz.objects.create(
            name='Test quiz name'
        )
        # Creates a Question instance.
        Question.objects.create(
            quizId=quiz.quizId,
            question='This is a test question.',
            choice1='This is a test choice 1.',
            choice2='This is a test choice 2.',
            choice3='This is a test answer.',
            choice4='This is a test choice 4.',
            answer='This is a test answer.',
            points=10
        )
        # Creates a Location instance.
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='test.png',
            qr_code_message='test_message_quiz',
        )
        setup_account(self)
        form_data = {
            'randomString': 'test_message_quiz',
        }
        response = self.client.post('/map/submit/', form_data)
        quiz_response = self.assertRedirects(response, '/quiz/1/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        # Check we get map template.
        self.assertTemplateUsed(quiz_response, '../quiz/templates/quiz.html')

    def test_submit_processing_page_loads(self):
        """Test if the submit processing page loads successfully"""
        response = self.client.get(reverse('submitView'))
        self.assertEqual(response.status_code, 200)
        # Check we get submitProcessing template.
        self.assertTemplateUsed(response, 'submitProcessing.html')

    def test_submit_processing_page_loads_on_incorrect_code(self):
        """Test if the submit processing page loads successfully"""
        setup_account(self)
        form_data = {
            'randomString': 'test_wrong_code'
        }
        response = self.client.post('/map/submit/', form_data)
        self.assertEqual(response.status_code, 200)
        # Check we get submitProcessing template.
        self.assertTemplateUsed(response, 'submitProcessing.html')


class StringFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""

    def test_valid_form(self):
        """Test if the form is valid"""
        # Creates a Location instance.
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='test.png',
            qr_code_message='mapRandomString',
        )
        form_data = {
            'randomString': 'mapRandomString'
        }
        form = StringForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        # Creates a Location instance.
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='Test.png',
            qr_code_message='mapRandomString',
            challengeId=0
        )
        # Checks that if all fields are empty, the form should not be valid.
        form_data = {
            'randomString': ''
        }
        form = StringForm(data=form_data)
        self.assertFalse(form.is_valid())
