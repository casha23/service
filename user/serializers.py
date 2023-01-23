from django.conf import settings
from django.contrib.auth import get_user_model

from rest_framework import serializers

# Get the UserModel

UserModel = get_user_model()


class UserDetailsSerializer(serializers.ModelSerializer):
    """
    User model w/o password
    """
    class Meta:
        model = UserModel
        fields = ('pk', 'phone_number', 'email', 'first_name', 'last_name', 'is_master')
        read_only_fields = ('email', )
