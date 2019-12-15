from rest_framework import generics

from CoreApp import models
from StatusApp.Comment_api import serializers


class CommentListAPIView(generics.ListAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentListSerializer


class CommentCreateAPIView(generics.CreateAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentDetailSerializer


class CommentDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                        = models.Comment.objects.all()
    serializer_class                = serializers.CommentDetailSerializer

    def get_serializer_context(self):
        return {'request': self.request}
