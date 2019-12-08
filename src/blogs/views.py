from django.shortcuts import render

from rest_framework import generics

from core.models import Blog
from blogs import serializers



class BlogCreateAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer
    permission_classes      = []
    authentication_classes  = []

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
        

class BlogsListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogListSerializer
    permission_classes      = []
    authentication_classes  = []
        

class BlogsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = serializers.BlogDetailSerializer
    permission_classes      = []
    authentication_classes  = []