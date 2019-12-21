from django.db.models import Prefetch
from rest_framework import generics, permissions

from config.permissions import IsOwnerStaffOrReadonly
from VehicleApp.fleet_api import serializers
from CoreApp.models import Fleet, Vehicle


class FleetListAPIView(generics.ListAPIView):
    serializer_class            = serializers.FleetListSerializers
    queryset                    = Fleet.objects.all()


class FleetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()
    permission_classes          = [IsOwnerStaffOrReadonly]

    def get_serializer_context(self):
        return {'request':self.request}


class AdminFleetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()
    permission_classes          = [permissions.IsAdminUser]

    def get_serializer_context(self):
        return {'request':self.request}


class FleetCreateAPIView(generics.CreateAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()
    permission_classes          = [permissions.IsAuthenticated]

    def get_serializer_context(self):
        return {'request':self.request}
