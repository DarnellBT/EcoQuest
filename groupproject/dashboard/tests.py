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
        'password2': 'secret_pass'
    }
    instance.client.post('/register/', register_form_data)
    form_data = {
        'username': 'JohnDoe@email.com',
        'password': 'secret_pass'
    }
    instance.client.post('/login/', form_data)


class DashboardViewTest(TestCase):
    """Class tests if pages load"""

    def test_account_page_loads(self):
        """Test if the account page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('account'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard template.
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_challenges_page_loads(self):
        """Test if the challenges page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('challenges'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard challenges template.
        self.assertTemplateUsed(response, 'dashboard_challenges.html')

    def test_change_name_page_loads(self):
        """Test if the change name page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('change-name'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard change name template.
        self.assertTemplateUsed(response, 'dashboard_name.html')

    def test_change_password_page_loads(self):
        """Test if the change password page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('change-password'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard change password template.
        self.assertTemplateUsed(response, 'dashboard_password.html')

    def test_change_username_page_loads(self):
        """Test if the change username page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('change-uname'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard change username template.
        self.assertTemplateUsed(response, 'dashboard_username.html')

    def test_login_page_redirect_loads_when_logout(self):
        """Test if the login page loads successfully when a user logs out."""
        setup_account(self)
        response = self.client.get(reverse('logout'))
        login_response = self.assertRedirects(response, 'login', status_code=302, target_status_code=404,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        response = self.client.get(reverse('account'))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')


class UsernameFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain UsernameFrom cases"""

    def test_change_username(self):
        """Test if the user can change their username"""
        setup_account(self)
        form_data = {
            'username': 'Pikachu'
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('change-uname'), form_data)
        user_profile = UserProfile.objects.get(userId=1)
        self.assertEqual(user_profile.user.username, 'Pikachu')


class NameFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain NameFrom cases"""

    def test_change_name(self):
        """Test if the user can change their name"""
        setup_account(self)
        form_data = {
            'username': 'Mewtwo',
            'first_name': 'Peter',
            'last_name': 'Parker',
            'email': 'i-am@email.com'
        }
        form = UserForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('edit_account'), form_data)
        user_profile = UserProfile.objects.get(userId=1)
        self.assertEqual(user_profile.user.first_name, 'Peter')
        self.assertEqual(user_profile.user.last_name, 'Parker')
        self.assertEqual(user_profile.user.first_name, 'Sarah')
        self.assertEqual(user_profile.user.last_name, 'Parker')


class PasswordFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain PasswordForm cases"""

    def test_change_password(self):
        """Test if the user can change their password"""
        setup_account(self)
        form_data = {
            'password': 'new_secret_pass',
        }
        form = PasswordForm(data=form_data)
        self.assertTrue(form.is_valid())
        self.client.post(reverse('change-password'), form_data)
        user_profile = UserProfile.objects.get(userId=1)
        self.assertTrue(user_profile.user.check_password('new_secret_pass'))
