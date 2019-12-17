from rest_framework import generics, permissions

from StatusApp.serializers import BlogListSerializer
from VehicleApp.vehicle_api.serializers import VehicleListSerializer
from CoreApp.models import Blog, Vehicle
    

class UserBlogListAPIView(generics.ListAPIView):
    pass
    serializer_class            = BlogListSerializer
    permission_classes          = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user             = self.request.user
        return Blog.objects.filter( user=user )
    

class UserVehicleListAPIView(generics.ListAPIView):
    pass
    serializer_class            = VehicleListSerializer
    permission_classes          = [permissions.IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        user             = self.request.user
        return Vehicle.objects.filter( user=user )
        