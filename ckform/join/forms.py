from django import forms
from django.forms import ModelForm
from .models import Join

class JoinForm(forms.ModelForm):
    first_name = forms.CharField(error_messages={'required': 'Please enter your first name'})
    last_name = forms.CharField(error_messages={'required': 'Please enter your last name'})
    email = forms.CharField(error_messages={'required': 'Please enter a valid email address'})
    zip_code = forms.CharField(error_messages={'required': 'Please enter a valid zipcode'})
    class Meta:
        model = Join
        fields = ['first_name', 'last_name', 'email', 'zip_code', 'receive_newsletter']