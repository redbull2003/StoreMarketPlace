# Third-party import
from rest_framework import serializers

# Local import
from Order.models import Order, OrderItem
from Account.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'phone_number')


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Order
        fields = ('id', 'user', 'created', 'is_paid')


class OrderItemSerializer(serializers.ModelSerializer):
    # user = UserSerializer()
    # order = OrderSerializer()

    class Meta:
        model = OrderItem
        fields = ('id', 'user', 'product', 'order', 'quantity')