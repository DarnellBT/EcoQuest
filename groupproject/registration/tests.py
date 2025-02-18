from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from .models import UserProfile
from .forms import RegistrationForm
from .views import register

class RegistrationModelTest(TestCase):
    def test_create_user_profile(self):
        """Test creating a UserProfile instance"""
        user = User.objects.create(
            username='Dragonite',
            first_name='John',
            last_name='Doe',
            email='JohnDoe@email.com',
        )

        user.set_password('secret_pass')
        user_profile = UserProfile.objects.create(user=user,)

        self.assertEqual(user_profile.userId, 1)
        self.assertEqual(user_profile.user, user)
        self.assertEqual(user_profile.points, 0)
        self.assertEqual(user_profile.is_user, 1)
        self.assertEqual(user_profile.is_game_keeper, 0)
        self.assertEqual(user_profile.is_admin, 0)

class RegistrationViewTest(TestCase):
    def test_registration_page_loads(self):
        """Test if the registration page loads successfully"""
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

class RegistrationFormTest(TestCase):
    def test_valid_form(self):
        """Test if the form is valid"""
        form_data = {'username': 'Dragonite', 'first_name': 'John', 'last_name': 'Doe', 'email': 'JohnDoe@email.com', 'password1': 'secret_pass', 'password2': 'secret_pass'}
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        form_data = {'username': '', 'first_name': '', 'last_name': '', 'email': '', 'password1': '', 'password2': ''}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        form_data = {'username': 'Dragonite', 'first_name': 'John', 'last_name': 'Doe', 'email': 'JohnDoe@email.com', 'password1': 'secret01', 'password2': 'secret02'}
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
