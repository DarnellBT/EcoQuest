from django import forms
from django.contrib.auth.models import User
from django.forms import ValidationError

class UsernameForm(forms.Form):
    username = forms.CharField(max_length=100, required=True)
    class Meta:
        fields = ['username']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exists():
            raise ValidationError(f"The email {username} is already taken")
        return username


class NameForm(forms.Form):
    firstName = forms.CharField(max_length=50, required=True)
    lastName = forms.CharField(max_length=50, required=True)

class PasswordForm(forms.Form):
    password = forms.CharField(max_length=50, required=True)