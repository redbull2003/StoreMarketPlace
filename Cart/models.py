# Standard library import
from django.db import models

# Local import
from Account.models import User
from Product.models import Product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user.username} - {self.product.title}'