from django.shortcuts import render

from rest_framework import generics, permissions, viewsets

from BlogApp import serializers
from CoreApp import models


##############################          BLOG TOPIC          #############################

class BlogTopicListAPIView(generics.ListAPIView):
    queryset                = models.BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryListSerializer
    permission_classes      = [permissions.IsAdminUser]


class BlogTopicCreationAPIView(generics.CreateAPIView):
    queryset                = models.BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryDetailSerializer
    permission_classes      = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BlogTopicDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = models.BlogTopic.objects.all()
    serializer_class        = serializers.BlogCategoryDetailSerializer
    permission_classes      = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


##############################          BLOG               #############################

class BlogListAPIView(generics.ListAPIView):
    queryset                = models.Blog.objects.filter(is_approved=True)
    serializer_class        = serializers.BlogListSerializer
    search_fields           = ('title', 'content')


class BlogCreationAPIView(generics.CreateAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer

    def get_serializer_context(self):
        return {'request':self.request}

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class AdminBlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = models.Blog.objects.all()
    serializer_class        = serializers.AdminBlogDetailSerializer

    def perform_update(self, serializer):
        serializer.save(approved_by=self.request.user)


        ###############################     COMMENT        ###############################

# class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset                = models.