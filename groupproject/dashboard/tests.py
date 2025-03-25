"""Module contains test cases for dashboard"""
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from registration.models import UserProfile

from .forms import UserForm


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


class DashboardViewTest(TestCase):
    """Class tests if pages load."""

    def test_account_page_loads(self):
        """Test if the account page loads successfully."""
        setup_account(self)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard template.
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_edit_details_page_loads(self):
        """Test if the edit details page loads successfully."""
        setup_account(self)
        response = self.client.get(reverse('edit_account'))
        self.assertEqual(response.status_code, 200)
        # Check we get edit details template.
        self.assertTemplateUsed(response, 'edit_details.html')

    def test_rewards_page_loads(self):
        """Test if the change rewards page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('rewards'))
        self.assertEqual(response.status_code, 200)
        # Check we get rewards template.
        self.assertTemplateUsed(response, 'rewards.html')

    def test_login_page_redirect_loads_when_logout(self):
        """Test if the main page loads successfully when a user logs out."""
        setup_account(self)
        response = self.client.get(reverse('logout'))
        main_response = self.assertRedirects(response, '/', status_code=302, target_status_code=200, fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(main_response, '../main/templates/home.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        response = self.client.get(reverse('account'))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')


class UsernameFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain UserFrom cases"""

    def test_change_username(self):
        """Test if the user can change their username"""
        setup_account(self)
        form_data = {
            'username': 'Pikachu',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
        }
        user_profile = UserProfile.objects.get(userId=1)
        form = UserForm(form_data, instance=user_profile.user)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('edit_account'), form_data)
        self.assertEqual(user_profile.user.username, 'Pikachu')

    def test_change_first_name(self):
        """Test if the user can change their firstname"""
        setup_account(self)
        form_data = {
            'username': 'Dragonite',
            'first_name': 'Peter',
            'last_name': 'Doe',
            'email': 'JohnDoe@email.com',
        }
        user_profile = UserProfile.objects.get(userId=1)
        form = UserForm(form_data, instance=user_profile.user)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('edit_account'), form_data)
        self.assertEqual(user_profile.user.first_name, 'Peter')

    def test_change_lastname(self):
        """Test if the user can change their lastname"""
        setup_account(self)
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Parker',
            'email': 'JohnDoe@email.com',
        }
        user_profile = UserProfile.objects.get(userId=1)
        form = UserForm(form_data, instance=user_profile.user)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('edit_account'), form_data)
        self.assertEqual(user_profile.user.last_name, 'Parker')

    def test_change_email(self):
        """Test if the user can change their email"""
        setup_account(self)
        form_data = {
            'username': 'Dragonite',
            'first_name': 'John',
            'last_name': 'Doe',
            'email': 'NewJohmDoe@email.com',
        }
        user_profile = UserProfile.objects.get(userId=1)
        form = UserForm(form_data, instance=user_profile.user)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('edit_account'), form_data)
        self.assertEqual(user_profile.user.email, 'NewJohmDoe@email.com')
