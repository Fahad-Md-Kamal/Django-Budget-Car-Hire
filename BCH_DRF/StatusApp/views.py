from datetime import datetime
from rest_framework import generics, serializers


from StatusApp import serializers as srl
from CoreApp.models import Blog, Comment


class BlogCreationAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.BlogDetailSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.BlogDetailSerializer

    def perform_update(self, serializer):
        serializer.save(updated_on = datetime.now())


class AdminBlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.AdminBlogDetailSerializer

    def perform_update(self, serializer):
        serializer.save(approved_by = self.request.user)


class BlogListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.BlogListSerializer
