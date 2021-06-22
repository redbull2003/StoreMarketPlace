# Third-party import 
from django.db.models import fields
from rest_framework import serializers

# Local import
from Product.models import Product

class ProductSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='api_product:retrieve')
    
    class Meta:
        model = Product
        fields = '__all__'  