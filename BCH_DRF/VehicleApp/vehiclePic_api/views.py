from rest_framework import generics

from config.permissions import IsVehicleOwnerReadonly
from VehicleApp.vehiclePic_api import serializers
from CoreApp.models import VehiclePics


class VehiclePictureListAPIView(generics.ListAPIView):
    serializer_class            = serializers.VehiclePictureSerializer
    queryset                    = VehiclePics.objects.all()


class VehiclePictureUploadAPIView(generics.CreateAPIView):
    serializer_class            = serializers.VehiclePictureUploadSerializer
    queryset                    = VehiclePics.objects.all()

    def get_serializer_context(self):
        return {'request': self.request}


class VehiclePictureDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class            = serializers.VehiclePictureUploadSerializer
    queryset                    = VehiclePics.objects.all()
    permission_classes          = [IsVehicleOwnerReadonly]
