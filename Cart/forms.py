# Standard library import
from django import forms

# Local import
from .models import Cart


class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)