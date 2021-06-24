# Third-party import
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse as api_reverse
from rest_framework import status

# Standard library import
from django.contrib.auth import get_user_model

# Local import
from Product.models import Product

User = get_user_model()

class ProductTestCase(APITestCase):
    def setUp(self):
        Product.objects.create(
            title='test',
            description='test',
            unit_price=500,
        )
    
    def test_product(self):
        product_count = Product.objects.count()
        self.assertEqual(product_count, 1)

    def test_get_list(self):
        # test the get list
        data = {}
        url = api_reverse('api_product:list')
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_create_product(self):
        # test the create product
        data = {'title': 'test', 'description': 'test'}
        url = api_reverse('api_product:create')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
    
    def test_retrieve_product(self):
        product = Product.objects.first()
        data = {}
        url = product.get_api_url()
        response = self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_update_product(self):
        data = {'title': 'test1', 'description': 'test'}
        url = api_reverse('api_product:update', args=[7])
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_delete_product(self):
        data = {'title': 'test1', 'description': 'test'}
        url = api_reverse('api_product:delete', args=[7])
        response = self.client.delete(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)