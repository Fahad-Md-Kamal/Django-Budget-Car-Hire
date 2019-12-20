from rest_framework import generics

from VehicleApp.fleet_api import serializers
from CoreApp.models import Fleet

# 
class FleetListAPIView(generics.ListAPIView):
    serializer_class            = serializers.FleetListSerializers
    queryset                    = Fleet.objects.all()


class FleetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()

    def get_serializer_context(self):
        return {'request':self.request}


class AdminFleetDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()

    def get_serializer_context(self):
        return {'request':self.request}


class FleetCreateAPIView(generics.CreateAPIView):
    serializer_class            = serializers.FleetCreateSerializers
    queryset                    = Fleet.objects.all()

    def get_serializer_context(self):
        return {'request':self.request}
