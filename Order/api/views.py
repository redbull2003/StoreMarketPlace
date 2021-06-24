# Third-party import
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
)
from rest_framework.permissions import IsAuthenticated
from rest_framework.mixins import ListModelMixin

# Local import
from .serializers import (
    OrderSerializer,
    OrderItemSerializer
)
from .permissions import IsOwner, IsAdminUser
from Order.models import Order, OrderItem


class OrderListView(ListAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAdminUser,)


class OrderRetrieveView(RetrieveAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)

    def get_object(self):
        pk = self.kwargs.get('pk')
        return Order.objects.get(pk=pk)


class OrderCreateView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class OrderItemCreateView(ListModelMixin, CreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class OrderUpdateView(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)


class OrderDestroyView(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = (IsOwner,)