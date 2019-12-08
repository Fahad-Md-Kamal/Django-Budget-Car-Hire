from django.shortcuts import render

from rest_framework import generics

from core.models import Blog
from blogs import serializers



class BlogCreateAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BlogsListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogListSerializer
        

class BlogsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer