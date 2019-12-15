from datetime import datetime
from rest_framework import generics, serializers, permissions

from config.permissions import IsOwnerStaffOrReadonly
from StatusApp import serializers as srl
from CoreApp.models import Blog, Comment


class BlogCreationAPIView(generics.CreateAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.BlogDetailSerializer
    permission_classes      = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.BlogDetailSerializer
    permission_classes      = [IsOwnerStaffOrReadonly]

    def perform_update(self, serializer):
        serializer.save(updated_on = datetime.now())


class AdminBlogDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                = Blog.objects.all()
    serializer_class        = srl.AdminBlogDetailSerializer
    permission_classes      = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(approved_by = self.request.user)


class BlogListAPIView(generics.ListAPIView):
    queryset                = Blog.objects.filter(is_approved=True)
    serializer_class        = srl.BlogListSerializer

    def get_serializer_context(self):
        return {'request':self.request}
