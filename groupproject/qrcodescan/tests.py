"""Module contains test cases for qrcodescan."""
from django.test import TestCase
from django.urls import reverse
from challenge.models import Challenge
from quiz.models import Quiz, Question
from map.models import Location


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


class TestQRCodeScan(TestCase):
    """Class tests if pages load"""

    def test_qr_code_scan_page_loads(self):
        """Test if qr code scan page loads"""
        setup_account(self)
        response = self.client.get(reverse('qr-scanner'))
        self.assertEqual(response.status_code, 200)
        # Check we get map template.
        self.assertTemplateUsed(response, 'scan.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        response = self.client.get(reverse('qr-scanner'))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')