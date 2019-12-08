from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    """
    User Public Details serializer
    """
    password            = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model           = User
        fields          = ( 'id',
                            'url',
                            'username', 
                            'email', 
                            'password', 
                            'is_active')


class UserLoginSerializer(UserPublicSerializer):
    """
    User Login serializer
    """
    class Meta:
        model           = User
        fields          = ( 'username', 
                            'email')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User Details serializer
    """
    class Meta:
        model           = User
        fields          = ( 'id', 
                            'url',
                            'username', 
                            'email', 
                            'first_name', 
                            'last_name')
