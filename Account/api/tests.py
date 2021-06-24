# Third-party import
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Standard library import
from django.contrib.auth import get_user_model

User = get_user_model()


class UserTestCase(APITestCase):
    def setUp(self):
        user = User(
            username='test',
            email='test@test.com',
        )
        user.set_password('RandomPass')
        user.save()

    def test_single_user(self):
        user_count = User.objects.count()
        self.assertEqual(user_count, 1)

    # def test_user_login(self):
    #     data = {
    #         'username': 'max',
    #         'password': 'max123',
    #         'token': 'sometoken'
    #     }
    #     url = api_reverse('api_account:sign_in')
    #     response = self.client.post(url, data)
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)