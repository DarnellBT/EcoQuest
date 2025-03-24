from django.test import TestCase
from django.urls import reverse


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


class LeaderboardViewTest(TestCase):
    """Class tests if pages load"""

    def test_leaderboard_page_loads(self):
        """Test if the leaderboard page loads successfully"""
        setup_account(self)
        response = self.client.get(reverse('leaderboard'))
        self.assertEqual(response.status_code, 200)
        # Check we get dashboard template.
        self.assertTemplateUsed(response, 'leaderboard.html')

    def test_login_page_redirect_loads_when_logout(self):
        """Test if the login page loads successfully when a user logs out."""
        setup_account(self)
        response = self.client.get(reverse('logout'))
        login_response = self.assertRedirects(response, 'login', status_code=302, target_status_code=404,
                                              fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(login_response, '../login/templates/loginPage.html')
