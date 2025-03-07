"""Module contains test cases for about"""
from django.test import TestCase
from django.urls import reverse


class SustainViewTest(TestCase):
    """Class tests if pages load"""

    def test_about_page_loads(self):
        """Test if the about page loads successfully"""
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
        response = self.client.get(reverse('about'))
        # Check we successfully load about at we also get the about template.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')

    def test_login_page_redirect_loads_if_not_logged_in(self):
        """Test if the login page loads successfully if a user is not logged in."""
        response = self.client.get(reverse('about'))
        login_response = self.assertRedirects(response, '/login', status_code=302, target_status_code=301,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')
