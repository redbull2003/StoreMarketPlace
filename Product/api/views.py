# Third-party import
from rest_framework.generics import (
    CreateAPIView,
    ListAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView
) 
from rest_framework.permissions import IsAdminUser
from rest_framework import filters

# local import
from .serializers import ProductSerializer
from Product.models import Product

class ProductListView(ListAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('title', 'description')
    ordering_fields = ('id',)


class ProductRetrieveView(RetrieveAPIView):
    queryset = Product.objects.filter(available=True)
    serializer_class = ProductSerializer


class ProductCreateView(CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


class ProductUpdateView(UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)


class ProductDestroyView(DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = (IsAdminUser,)