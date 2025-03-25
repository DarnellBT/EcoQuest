"""Module contains test cases for map"""
from django.test import TestCase
from django.urls import reverse
from .models import Location


class MapModelTest(TestCase):
    """Class contains tests that use assert to test map model"""

    def test_create_location(self):
        """Test creating a Location instance"""
        # Creates a Location instance.
        location = Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            icon='computer'
        )
        self.assertEqual(location.name, 'test_location')
        self.assertEqual(location.latitude, 50.2)
        self.assertEqual(location.longitude, -3.04)
        self.assertEqual(location.icon, 'computer')


class MapViewTest(TestCase):
    """Class tests if pages load"""

    def test_map_page_loads(self):
        """Test if the map page loads successfully"""
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)
        # Check we get map template.
        self.assertTemplateUsed(response, 'map.html')
