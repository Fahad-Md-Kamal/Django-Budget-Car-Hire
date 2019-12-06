from rest_framework import serializers
from core import models



class UserPublicSerializer(serializers.ModelSerializer):
    """
    Serializes User Details
    """
    password            = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model           = models.User
        fields          = ( 'id', 
                            'username', 
                            'email', 
                            'password')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Serializes User Details
    """
    class Meta:
        model           = models.User
        fields          = ( 'id', 
                            'url',
                            'username', 
                            'email', 
                            'first_name', 
                            'last_name')
