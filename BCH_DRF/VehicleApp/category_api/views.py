
from rest_framework import generics, permissions

from VehicleApp.category_api import serializers
from CoreApp.models import VehicleCategory

class VehicleCategoryListAPIView(generics.ListAPIView):
    queryset                    = VehicleCategory.objects.all()
    serializer_class            = serializers.CategoryListSerializer
    search_fields               = ('name', 'description')


class VehicleCategoryDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset                    = VehicleCategory.objects.all()
    serializer_class            = serializers.CategoryDetailSerializer
    permission_classes          = [permissions.IsAdminUser]

    def perform_update(self, serializer):
        serializer.save(updated_by=self.request.user)


class VehicleCategoryCreateAPIView(generics.CreateAPIView):
    queryset                    = VehicleCategory.objects.all()
    serializer_class            = serializers.CategoryDetailSerializer
    permission_classes          = [permissions.IsAdminUser]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)