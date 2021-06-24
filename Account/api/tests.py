# Third-party import
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse

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