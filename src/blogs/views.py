from django.shortcuts import render

from rest_framework import generics, permissions, mixins

from core.models import Blog
from core.permissions import IsDataOwnerOrReadOnly
from blogs import serializers



class BlogCreateAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogCreateSerializer
    permission_classes      = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BlogsListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogListSerializer
    search_fields           = ('title', 'content')
        

class BlogsAdminDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogAdminDetailSerializer
    permission_classes      = [permissions.IsAdminUser]


class BlogsUserDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class        = serializers.BlogPublicDetailSerializer
    permission_classes      = [IsDataOwnerOrReadOnly]
    queryset                = Blog.objects.all()


class RequestUserBlogListAPIView(generics.ListAPIView):
    serializer_class        = serializers.BlogInLineSerializer
    search_fields           = ('title', 'content')

    def get_queryset(self, *args, **kwargs):
        return Blog.objects.filter(user__username=self.request.user.username)


