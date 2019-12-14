from datetime import datetime
from rest_framework import generics, permissions

from CoreApp import models
from config.permissions import IsOwnerStaffOrReadonly
from BlogApp.comment import serializers


class CommentCreateAPIView(generics.CreateAPIView):
    serializer_class        = serializers.CommentCreateSerializer
    queryset                = models.Comment.objects.all()
    permission_classes      = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class        = serializers.CommentDetailSerializer
    queryset                = models.Comment.objects.all()


    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, 
                        updated_on = datetime.now())

    def get_serializer_context(self):
        return {'request':self.request}