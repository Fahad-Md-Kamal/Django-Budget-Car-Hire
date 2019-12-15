from datetime import datetime
from rest_framework import generics, permissions

from config.permissions import IsOwnerStaffOrReadonly
from CoreApp import models
from StatusApp.Comment_api import serializers


class CommentListAPIView(generics.ListAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentListSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentDetailSerializer
    permission_classes              = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentDetailSerializer
    permission_classes              = [IsOwnerStaffOrReadonly]

    def perform_update(self, serializer):
        serializer.save(updated_on = datetime.now())

