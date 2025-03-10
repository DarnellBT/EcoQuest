"""Module contains test cases for sustain"""
from django.test import TestCase
from django.urls import reverse


class SustainViewTest(TestCase):
    """Class tests if pages load"""

    def test_sustainability_page_loads(self):
        """Test if the sustainability page loads successfully"""
        response = self.client.get(reverse('sustainability'))
        self.assertEqual(response.status_code, 200)
        # Check we get sustainability template.
        self.assertTemplateUsed(response, 'sustain.html')
