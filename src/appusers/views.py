from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, views, permissions

from core.models import User
from appusers import serializers

AppUser = get_user_model()

class UserRegisterAPIView(generics.CreateAPIView):
    """
    CREATE user information
    """
    permission_classes          = []
    authentication_classes      = []
    queryset                    = AppUser.objects.all()
    serializer_class            = serializers.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles post request to create users
        """
        return self.create(request, *args, **kwargs)


class UserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    DETAIL and UPDATE User Information
    """
    permission_classes          = []
    authentication_classes      = []
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailSerializer

    def put(self, request, *args, **kwargs):
        """
        Handles user `PUT` request
        """
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """
        Handles user `PATCH` request
        """
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """
        Handles users `Delete` request
        """
        return self.destroy(request, *args, **kwargs)


class UserListAPIView(generics.ListAPIView):
    """
    LIST of user information
    """
    permission_classes          = []
    authentication_classes      = []
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserPublicSerializer


