from django import forms

class ContactForm(forms.Form):
    """Contact Form with first name, email, message to send emails"""
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': "Name"}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={'placeholder': "Email"}))
    message = forms.CharField(label="Message", max_length=1000, required=True, widget=forms.Textarea(attrs={"placeholder": "Message"}))