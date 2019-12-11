from django.shortcuts import render

from rest_framework import generics

from CoreApp.models import User
from AppUsers import serializers


class UserCreateAPIView(generics.CreateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserCreateSerializer


class UsersListAPIView(generics.ListAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserListSerializer


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailSerializer


class UserDetailAdminAPIView(generics.RetrieveUpdateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailAdminSerializer
