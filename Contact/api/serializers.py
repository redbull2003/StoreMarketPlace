# Third-party import
from rest_framework import serializers

# Local import
from Contact.models import Contact


class ContactSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='api_contact:rud')

    class Meta:
        model = Contact
        fields = '__all__'