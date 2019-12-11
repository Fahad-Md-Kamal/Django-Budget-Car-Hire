from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics

from AppUsers import serializers

User = get_user_model()
class UserCreateAPIView(generics.CreateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserCreateSerializer


class UsersListAPIView(generics.ListAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserListSerializer


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailSerializer


class UserDetailAdminAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailAdminSerializer
