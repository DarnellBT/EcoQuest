"""Module contains test cases for main"""
from django.test import TestCase
from django.urls import reverse


class MainViewTest(TestCase):
    """Class tests if pages load"""

    def test_main_page_loads(self):
        """Test if the main page loads successfully"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'home.html')
