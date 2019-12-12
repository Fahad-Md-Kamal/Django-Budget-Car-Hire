from django.shortcuts import render
from django.contrib.auth import get_user_model

from rest_framework import generics, permissions as rest_permissions

from config import permissions
from CoreApp.models import ProfilePics
from AppUsers import serializers

User = get_user_model()
class UserCreateAPIView(generics.CreateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserCreateSerializer
    permission_classes          = [rest_permissions.AllowAny]

class UsersListAPIView(generics.ListAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserListSerializer
    search_fields               = ('username', 'email')


class UserDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailSerializer
    permission_classes          = [permissions.IsOwnerStaffOrReadonly]


class UserDetailStaffAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailStaffSerializer
    permission_classes          = [permissions.IsOwnerStaffOrReadonly]


class UserDetailAdminAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserDetailAdminSerializer
    permission_classes          = [rest_permissions.IsAdminUser]
