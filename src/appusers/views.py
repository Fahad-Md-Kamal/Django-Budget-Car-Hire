from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import generics, mixins, views, permissions, status
from rest_framework.response import Response

from core.models import User
from appusers import serializers

AppUser = get_user_model()

class UserRegisterAPIView(generics.CreateAPIView):
    """
    CREATE user information
    """
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
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserPublicSerializer


class UserLoginAPIView(views.APIView):
    permission_classes  = [permissions.AllowAny]
    serializer_class    = serializers.UserLoginSerializer

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer    = serializers.UserLoginSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            new_data = serializer.data
            return Response(new_data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
