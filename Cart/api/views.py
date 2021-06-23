# Third-party import
from django.http import request
from rest_framework import permissions, serializers
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated

# Local import
from .serializers import (
    CartSerializer,
    CreateCartSerializer,
    UpdateCartSerializer,
)
from .permissions import IsOwner, IsAdminUser
from Cart.models import Cart

class CartListView(ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsAdminUser,)


class CartRetrieveView(RetrieveAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)


class CartCreateView(CreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = CreateCartSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CartUpdateView(UpdateAPIView):
    queryset = Cart.objects.all()
    serializer_class = UpdateCartSerializer
    permission_classes = (IsOwner,)


class CartDestroyView(DestroyAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    permission_classes = (IsOwner,)