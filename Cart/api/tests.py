# Third-party import
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Standard library import
from django.contrib.auth import get_user_model

# Local import
from Cart.models import Cart
from Product.models import Product

User = get_user_model()


class CartTestCase(APITestCase):
    def setUp(self):
        self.user = User(
            username='test',
            email='test@test.com'
        )
        self.user.set_password('RandomPass')
        self.user.save()
        self.product = Product(
            title='abc',
            description='abcabc',
            unit_price=1000
        )
        self.product.save()
        Cart.objects.create(
            user=self.user,
            product=self.product,
            quantity=2
        )
    
    def test_cart(self):
        cart_count = Cart.objects.count()
        self.assertEqual(cart_count, 1)
    
    def test_cart_list(self):
        data = {}
        url = api_reverse('api_cart:list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_cart_create(self):
        data = {'user': self.user.username, 'product': self.product.title, 'quantity': 7}
        url = api_reverse('api_cart:create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_retrieve_cart(self):
        data = {}
        url = api_reverse('api_cart:retrieve', args=[1])
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_update_cart(self):
        data = {'quantity': 5}
        url = api_reverse('api_cart:update', args=[1])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_cart(self):
        data = {}
        url = api_reverse('api_cart:delete', args=[1])
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)