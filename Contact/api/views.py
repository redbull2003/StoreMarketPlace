# Third-party import
from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
)

# Local import
from .serializers import ContactSerializer
from Contact.models import Contact
from Account.api.permissions import IsStaff


class ContactListAPI(ListAPIView):
    queryset = Contact.objects.all()

    def get_serializer(self, *args, **kwargs):
        serializer_class = ContactSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)


class ContactRUDAPI(RetrieveUpdateDestroyAPIView):
    queryset = Contact.objects.all()
    permission_classes = (IsStaff,)

    def get_serializer(self, *args, **kwargs):
        serializer_class = ContactSerializer
        kwargs['context'] = self.get_serializer_context()
        return serializer_class(*args, **kwargs)