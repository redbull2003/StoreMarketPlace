# Standard library import
from django import forms
from django.forms import fields

# Local import
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'