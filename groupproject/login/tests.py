"""Module contains test cases for login"""
from django.test import TestCase
from django.urls import reverse
from .forms import LoginForm


def setup_registration(instance):
    """Sets up the user registration"""
    register_form_data = {
        'username': 'Dragonite',
        'first_name': 'John',
        'last_name': 'Doe',
        'email': 'JohnDoe@email.com',
        'password1': 'secret_pass',
        'password2': 'secret_pass'
    }
    # Registers user.
    instance.client.post('/register/', register_form_data)


class LoginViewTest(TestCase):
    """Class tests if pages load"""

    def test_login_page_loads(self):
        """Test if the login page loads successfully"""
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200, 'Login page did not load successfully.')
        # Check we get login template.
        self.assertTemplateUsed(response, 'loginPage.html', 'Login page did not load template successfully.')

    def test_home_page_redirect_loads(self):
        """Test if the login page loads successfully"""
        setup_registration(self)

        form_data = {
            'username': 'JohnDoe@email.com',
            'password': 'secret_pass'
        }

        response = self.client.post('/login/', form_data)
        login_response = self.assertRedirects(response, '/home/', status_code=302, target_status_code=200,
                                              fetch_redirect_response=True,
                                              msg_prefix='Login page did not redirect to home page successfully.')
        # Check we get home template.
        self.assertTemplateUsed(login_response, '../main/templates/home.html',
                                'Home page did not load template successfully.')


class LoginFormTest(TestCase):
    """Class tests if a form is invalid or valid in certain cases"""

    def test_valid_form(self):
        """Test if the form is valid"""
        setup_registration(self)

        form_data = {
            'username': 'JohnDoe@email.com',
            'password': 'secret_pass'
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        """Test if an invalid form is rejected"""
        setup_registration(self)
        # Checks that if all fields are empty, the form should not be valid.
        form_data = {
            'username': '',
            'password': ''
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Checks that if password is not correct, the form should not be valid.
        form_data = {
            'username': 'JohnDoe@email.com',
            'password': 'secret_wrong'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        # Checks that if email is not correct, the form should not be valid.
        form_data = {
            'username': 'JohnDoe@email.wrong',
            'password': 'secret_pass'
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
