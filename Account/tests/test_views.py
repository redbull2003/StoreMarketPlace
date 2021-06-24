# Standard library import
from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

# Local import
from Account.forms import SignUpForm
from Account.models import Profile

User = get_user_model()


class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_user_SignUp_GET(self):
        response = self.client.get(reverse('account:sign_up'))
        self.assertEqual(response.status_code, 200)
        self.failUnless(response.text['form'], SignUpForm)

    def test_user_SignUp_POST_valid(self):
        response = self.client.post(reverse('users:sign_up'), data={
            'username': 'jack',
            'email': 'jack@email.com',
            'password': 'jack',
            'confirm_password': 'jack'
        })
        self.assertEqual(response.status_code, 200)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Profile.objects.count(), 1)