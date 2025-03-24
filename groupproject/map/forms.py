from django import forms


class StringForm(forms.Form):
    randomString = forms.CharField(label='QR String', max_length=50)
