from django.shortcuts import render
from rest_framework import generics, mixins, views

from core.models import User
from appusers import serializers


class UserDetailAPIView(mixins.UpdateModelMixin, 
                        mixins.DestroyModelMixin, 
                        generics.RetrieveAPIView):
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


