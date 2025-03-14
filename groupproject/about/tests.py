"""Module contains test cases for about"""
from django.test import TestCase
from django.urls import reverse


class AboutViewTest(TestCase):
    """Class tests if pages load"""

    def test_about_page_loads(self):
        """Test if the about page loads successfully"""
        response = self.client.get(reverse('contact'))
        # Check we successfully load about at we also get the about template.
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'about.html')
