# Standard library import
from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator

# Local import
from Account.models import User
from Product.models import Product

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    is_paid = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)], null=True, blank=True)

    def __str__(self):
        return f'{self.user}'

    @property
    def get_total_price(self):
        total = sum(i.price() for i in self.order_item.all())
        if self.discount:
            discount_price = (self.discount * total) / 100
            return int(total - discount_price)
        return total


class OrderItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='order_item')
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user} - {self.product.title}'


class Coupon(models.Model):
    code = models.CharField(max_length=30, unique=True)
    start = models.DateTimeField()
    end = models.DateTimeField()
    active = models.BooleanField(default=False)
    discount = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    def __str__(self):
        return self.code