from django.shortcuts import render

from rest_framework import generics, permissions, viewsets

from BlogApp import serializers
from CoreApp.models import BlogTopic, Blog


##############################          BLOG TOPIC          #############################

class BlogTopicListAPIView(generics.ListAPIView):
    queryset                = BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryListSerializer
    permission_classes      = [permissions.IsAdminUser]


class BlogTopicCreationAPIView(generics.CreateAPIView):
    queryset                = BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryDetailSerializer
    permission_classes      = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BlogTopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryDetailSerializer
    permission_classes      = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


##############################          BLOG               #############################

class BlogListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.filter(is_approved=True)
    serializer_class        = serializers.BlogListSerializer
    search_fields           = ('title', 'content')


class BlogCreationAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class AdminBlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.AdminBlogDetailSerializer

    def perform_update(self, serializer):
        serializer.save(approved_by=self.request.user)