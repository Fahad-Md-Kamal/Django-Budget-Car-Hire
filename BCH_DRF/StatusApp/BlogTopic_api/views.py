from datetime import datetime
from rest_framework import generics, permissions

from config.permissions import IsOwnerStaffOrReadonly
from CoreApp.models import BlogTopic
from StatusApp.BlogTopic_api import serializers as srl


class BlogTopicCreateAPIView(generics.CreateAPIView):
    serializer_class            = srl.BlogTopicDetailSerializer
    queryset                    = BlogTopic.objects.all()
    permission_classes          = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class BlogTopicRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = srl.BlogTopicDetailSerializer
    queryset                    = BlogTopic.objects.all()
    permission_classes          = [IsOwnerStaffOrReadonly]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated_on = datetime.now())


class BlogTopicListAPIView(generics.ListAPIView):
    serializer_class            = srl.BlogListSerializer
    queryset                    = BlogTopic.objects.all()
