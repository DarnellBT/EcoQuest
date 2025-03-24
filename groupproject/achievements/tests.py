"""Module contains test cases for about"""
from django.test import TestCase
from django.urls import reverse


class AchievementViewTest(TestCase):
    """Class tests if pages load"""

    def test_achievement_page_loads(self):
        """Test if the achievement page loads successfully"""
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
        self.client.post('/register/', register_form_data)
        form_data = {
            'username': 'JohnDoe@email.com',
            'password': 'secret_pass'
        }
        self.client.post('/login/', form_data)

        response = self.client.get(reverse('achievements'))
        # Check we successfully load about at we also get the contact template.
        self.assertEqual(response.status_code, 200, 'The contact page did not load successfully.')
        self.assertTemplateUsed(response, 'achievements.html', 'The achievements.html template did not load successfully.')
