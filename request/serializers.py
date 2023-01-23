from user.serializers import UserDetailsSerializer
from rest_framework import serializers

from .models import Invoice, Request

# Serializers for Request

class ReguestForUserSerializer(serializers.ModelSerializer):
    """
    Request model for user
    """

    status = serializers.CharField(
        source='get_status_display', read_only=True
    )

    class Meta:
        model = Request
        fields = ('pk', 'phone_model', 'problem_description', 'status')


class ReguestForMasterSerializer(serializers.ModelSerializer):
    """
    Request model for master
    """

    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ('pk', 'phone_model', 'problem_description', 'status', 'user')
        read_only_fields = ('phone_model', 'problem_description')


# Serializers for Invoice

class InvoiceSerializer(serializers.ModelSerializer):
    """
    Invoice model for master
    """

    status = serializers.CharField(
        source='get_status_display', read_only=True
    )

    class Meta:
        model = Invoice
        fields = ('pk', 'request', 'price', 'status')
