from rest_framework import generics

from config.permissions import IsOwnerStaffOrReadonly
from CoreApp.models import Replay
from BlogApp. replay_api import serializers


class RepalyDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.ReplaysDetailSerializer
    queryset                    = Replay.objects.all()
    permission_classes          = [IsOwnerStaffOrReadonly]


class RepalyCreateAPIView(generics.CreateAPIView):
    serializer_class            = serializers.ReplayCreateSerializer
    queryset                    = Replay.objects.all()
