from datetime import datetime
from rest_framework import generics, permissions

from CoreApp.models import VehicleModel
from VehicleApp.vehicleModel_api import serializers


class VehicleModelListAPIView(generics.ListAPIView):
    queryset                    = VehicleModel.objects.all()
    serializer_class            = serializers.VehicleModelListSerializer


class VehicleModelCreateAPIView(generics.CreateAPIView):
    queryset                    = VehicleModel.objects.all()
    serializer_class            = serializers.VehicleModelSerializer
    permission_classes          = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


class VehicleModelDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                    = VehicleModel.objects.all()
    serializer_class            = serializers.VehicleModelSerializer
    permission_classes          = [permissions.IsAdminUser]
    search_fields               = ('name', 'description')

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user, updated_on = datetime.now())
