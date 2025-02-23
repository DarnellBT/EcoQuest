"""Module contains test cases for map"""
from django.test import TestCase
from django.urls import reverse
from .models import Location
from .forms import StringForm


class MapModelTest(TestCase):
    """Class contains tests that use assert to test map model"""
    def test_create_location(self):
        """Test creating a Location instance"""
        # Creates a Location instance
        location = Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='Test.png',
            qr_code_message='mapRandomString',
            challengeId=0
        )

        self.assertEqual(location.name, 'test_location')
        self.assertEqual(location.latitude, 50.2)
        self.assertEqual(location.longitude, -3.04)
        self.assertEqual(location.qr_code, 'Test.png')
        self.assertEqual(location.qr_code_message, 'mapRandomString')
        self.assertEqual(location.challengeId, 0)


class MapViewTest(TestCase):
    """Class tests if pages load"""
    def test_map_page_loads(self):
        """Test if the map page loads successfully"""
        response = self.client.get(reverse('map'))
        self.assertEqual(response.status_code, 200)
        # Check we get registration template.
        self.assertTemplateUsed(response, 'map.html')


class StringFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""
    def test_valid_form(self):
        """Test if the form is valid"""
        # Creates a Location instance
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='Test.png',
            qr_code_message='mapRandomString',
            challengeId=0
        )
        form_data = {
            'randomString': 'mapRandomString'
        }
        form = StringForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        # Creates a Location instance
        Location.objects.create(
            name='test_location',
            latitude=50.2,
            longitude=-3.04,
            qr_code='Test.png',
            qr_code_message='mapRandomString',
            challengeId=0
        )
        # Checks that if all fields are empty, the form should not be valid
        form_data = {
            'randomString': ''
        }
        form = StringForm(data=form_data)
        self.assertFalse(form.is_valid())
