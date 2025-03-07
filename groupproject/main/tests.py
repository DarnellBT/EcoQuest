"""Module contains test cases for main"""
from django.test import TestCase
from django.urls import reverse


class MainViewTest(TestCase):
    """Class tests if pages load"""

    def test_main_page_loads(self):
        """Test if the main page loads successfully"""
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
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'home.html')
