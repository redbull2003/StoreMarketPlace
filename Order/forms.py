# Standrad library import
from django import forms

# Local import
from .models import Coupon


class CouponForm(forms.ModelForm):
    class Meta:
        model = Coupon
        fields = ('code',)