from rest_framework import generics, permissions

from config.permissions import IsOwnerStaffOrReadonly
from VehicleApp.vehicle_api import serializers
from CoreApp.models import Vehicle


class VehicleListAPIView(generics.ListAPIView):
    serializer_class                = serializers.VehicleListSerializer
    queryset                        = Vehicle.objects.filter(is_approved=True, is_hired=False)
    # queryset                        = Vehicle.objects.all()
    search_fields                   = ( 'model__name', 
                                        'category__name', 
                                        'registration_no', 
                                        'rent', 
                                        'capacity')

    def get_serializer_context(self):
        return {'request': self.request}

class VehicleCreateAPIView(generics.CreateAPIView):
    serializer_class                = serializers.VehicleSerializer
    queryset                        = Vehicle.objects.all()
    permission_classes              = [permissions.IsAuthenticated]


class VehicleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class                = serializers.VehicleSerializer
    queryset                        = Vehicle.objects.all()
    permission_classes              = [IsOwnerStaffOrReadonly]

    def get_serializer_context(self):
        return {'request': self.request}

class ADMINVehicleDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class                = serializers.ADMINVehicleSerializer
    queryset                        = Vehicle.objects.all()
    permission_classes              = [permissions.IsAdminUser]