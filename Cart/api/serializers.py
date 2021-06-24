# Third-party import
from rest_framework import serializers

# Local import
from Cart.models import Cart
from Product.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'title',
            'unit_price',
            'amount',
            'discount',
            'total_price',
        )


class CartSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ('id', 'user', 'product', 'quantity')


class CreateCartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity')

        extra_kwargs  = {
            'user': {'write_only': True}
        }


class UpdateCartSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Cart
        fields = ('user', 'product', 'quantity')