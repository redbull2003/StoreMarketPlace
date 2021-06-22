# Standard-library import
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

# Third-party import
from captcha.fields import CaptchaField

# Local import
from .models import User


message = {
    'invalid': 'Please enter a valid email',
    'required': 'This field is required',
    'max_length': 'Carachter of this field is too long'
}


class UserCreationForm(forms.ModelForm):
    """A form for creating new users. Includes all the required
    fields, plus a repeated password."""
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    disabled password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('username', 'email')


class SignUpForm(forms.Form):
    username = forms.CharField(
        error_messages=message, label='نام کاربری', widget=forms.TextInput()
        )
    email = forms.EmailField(
        error_messages=message, label='ادرس ایمیل', widget=forms.TextInput()
        )
    password = forms.CharField(
        error_messages={'required': 'this field is required'}, 
        label='رمز عبور', widget=forms.PasswordInput()
        )
    confirm_password = forms.CharField(
        error_messages={'required': 'this field is required'}, 
        label='تایید رمز عبور', widget=forms.PasswordInput()
        )

    def clean_username(self):
        username = self.cleaned_data.get('username')
        qs = User.objects.get(username=username)

        if qs.exists():
            raise forms.ValidationError(' نام کاربری وارد شده قبلا ثبت شده است')
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.get(email=email)

        if qs.exists():
            raise forms.ValidationError('ایمیل وارد شده قبلا ثبت شده است')
        return email
    
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError('رمز عبور های وارد شده مطابقت ندارند')
        return confirm_password


class SignInForm(forms.Form):
    username = forms.CharField(label='نام کاربری', widget=forms.TextInput())
    password = forms.CharField(label='رمز عبور', widget=forms.PasswordInput())
    remember = forms.CharField(
        label='من را به یاد داشته باش', required=False,
        widget=forms.CheckboxInput()
    )
    captcha = CaptchaField() 


class UserProfileform(forms.ModelForm):
    def __init__(self, *args, **kwargs):

        self.fields['username'].disable = True
        self.fields['email'].disable = True

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'phone_number',
            'first_name',
            'last_name',
            'address',
            'country',
            'city',
        )