"""Module contains test cases for registration"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .forms import RegistrationForm
from .models import UserProfile


class RegistrationModelTest(TestCase):
    """Class contains tests that use assert to test registration model"""

    def test_create_user_profile(self):
        """Test creating a UserProfile instance"""
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
        self.assertEqual(user_profile.userId, 1)
        self.assertEqual(user_profile.user, user)
        self.assertEqual(user_profile.points, 0)
        self.assertEqual(user_profile.is_user, 1)
        self.assertEqual(user_profile.is_game_keeper, 0)
        self.assertEqual(user_profile.is_admin, 0)
        self.assertTrue(user_profile.user.check_password('secret_pass'))


class RegistrationViewTest(TestCase):
    """Class tests if pages load"""

    def test_registration_page_loads(self):
        """Test if the registration page loads successfully"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'registration.html')

    def test_login_page_redirect_loads(self):
        """Test if the login page loads successfully"""
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        }

        response = self.client.post('/register/', form_data)
        login_response = self.assertRedirects(response, '/login/', status_code=302, target_status_code=200,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')


class RegistrationFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""

    def test_valid_form(self):
        """Test if the form is valid"""
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret_pass',
            'password2': 'secret_pass'
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        # Checks that if all fields are empty, the form should not be valid
        form_data = {
            'username': '',
            'first_name': '',
            'last_name': '',
            'email': '',
            'password1': '',
            'password2': ''
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Checks that if passwords do not match, the form should not be valid.
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'secret01',
            'password2': 'secret02'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Checks that if passwords are less than 8 characters, the form should not be valid.
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
            'password1': 'short!!',
            'password2': 'short!!'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
