from django.test import TestCase
from Account.forms import SignUpForm


class TestSignUpForm(TestCase):
    def test_valid_data(self):
        form = SignUpForm(data={
            'username': 'kevin',
            'email': 'kevin@email.com',
            'password': 123,
            'confirm_password': 123
        })
        self.assertTrue(form.is_valid())
    
    def test_invalid_data(self):
        form = SignUpForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)