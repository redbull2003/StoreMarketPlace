# Standard library import
from django.db import models
from django.db.models.deletion import CASCADE

# Local import
from Account.models import User
from Product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user}'


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} - {self.product.title}'