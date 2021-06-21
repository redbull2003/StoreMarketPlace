# Standard-library import
from django import forms


class Searchform(forms.Form):
    search = forms.CharField(widget=forms.TextInput())