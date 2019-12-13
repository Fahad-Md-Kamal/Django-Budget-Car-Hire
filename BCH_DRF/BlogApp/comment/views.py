from datetime import datetime
from rest_framework import generics, permissions

from CoreApp import models
from config.permissions import IsOwnerStaffOrReadonly
from BlogApp.comment import serializers

class ParentCommentCreateAPIView(generics.CreateAPIView):
    serializer_class        = serializers.CommentDetailSerializer
    queryset                = models.Comment.objects.all()
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ChildCommentCreateAPIView(generics.CreateAPIView):
    serializer_class        = serializers.ChildCommentSerializer
    queryset                = models.Comment.objects.all()
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ParentCommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class        = serializers.ParentCommentSerializer
    queryset                = models.Comment.objects.all()
    permission_classes      = [IsOwnerStaffOrReadonly]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, 
                        updated_on = datetime.now())


class CommentListAPIView(generics.ListAPIView):
    serializer_class        = serializers.ParentCommentSerializer
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]

    