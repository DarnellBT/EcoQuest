from django import forms

class ImageUpload(forms.Form):
    image = forms.ImageField(required=True)