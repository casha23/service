from user.serializers import UserDetailsSerializer
from rest_framework import serializers

from .models import Request


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
    Request model for user
    """

    user = UserDetailsSerializer(read_only=True)

    class Meta:
        model = Request
        fields = ('pk', 'phone_model', 'problem_description', 'status', 'user')
        read_only_fields = ('phone_model', 'problem_description')
