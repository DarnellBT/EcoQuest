"""Module contains test cases for about"""
from django.test import TestCase
from django.urls import reverse
from .forms import ContactForm


class AboutViewTest(TestCase):
    """Class tests if pages load"""

    def test_about_page_loads(self):
        """Test if the about page loads successfully"""
        response = self.client.get(reverse('contact'))
        # Check we successfully load about at we also get the contact template.
        self.assertEqual(response.status_code, 200, 'The contact page did not load successfully')
        self.assertTemplateUsed(response, 'contact.html', 'The contact.html template did not load successfully')

    def test_main_page_redirect_loads(self):
        """Test if the main page loads successfully"""
        form_data = {
            'first_name': 'John',
            'email': 'JohnDoe@email.com',
            'message': 'This is a test message.'
        }
        response = self.client.post('/contact/', form_data)
        main_response = self.assertRedirects(response, '/contact/', status_code=302, target_status_code=200,
                                             fetch_redirect_response=True)
        # Check we get loginPage template.
        self.assertTemplateUsed(main_response, '../main/templates/home.html')


class ContactFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""

    def test_valid_form(self):
        """Test if the form is valid"""
        form_data = {
            'first_name': 'John',
            'email': 'JohnDoe@email.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_no_name_invalid_form(self):
        """Test if the form is invalid without name"""
        form_data = {
            'first_name': '',
            'email': 'JohnDoe@email.com',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_no_email_invalid_form(self):
        """Test if the form is invalid without email"""
        form_data = {
            'first_name': 'John',
            'email': '',
            'message': 'This is a test message.'
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())

    def test_no_message_invalid_form(self):
        """Test if the form is invalid without message"""
        form_data = {
            'first_name': 'John',
            'email': 'JohnDoe@email.com',
            'message': ''
        }
        form = ContactForm(data=form_data)
        self.assertFalse(form.is_valid())
