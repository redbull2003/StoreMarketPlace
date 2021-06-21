# Standard library import
from django.test import SimpleTestCase
from django.urls import resolve, reverse

# Local import 
from Product import views


class TestUrls(SimpleTestCase):
    def test_product_list(self):
        url = reverse('product:list')
        self.assertEqual(resolve(url).func, views.product_list)

    def test_product_detail(self):
        url = reverse('product:detail', args=['test', 7])
        self.assertEqual(resolve(url).func, views.product_detail)