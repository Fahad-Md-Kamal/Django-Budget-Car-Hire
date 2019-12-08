from django.shortcuts import render

from rest_framework import generics, permissions

from core import models, permissions as custom_permissions
from blogs import serializers



class BlogCreateAPIView(generics.CreateAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogCreateSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BlogsListAPIView(generics.ListAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogListSerializer
        

class BlogsAdminDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogAdminDetailSerializer
    permission_classes      = [permissions.IsAdminUser]
        

class BlogsUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogPublicDetailSerializer
    permission_classes      = [custom_permissions.IsDataOwnerOrReadOnly]