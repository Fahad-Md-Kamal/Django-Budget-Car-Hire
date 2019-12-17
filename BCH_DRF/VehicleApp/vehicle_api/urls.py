from django.urls import path, include

from VehicleApp.vehicle_api import views

urlpatterns =[
    path(   '', 
            views.VehicleListAPIView.as_view(), 
            name='vehicle-list'),

    path(   '<int:pk>/', 
            views.VehicleDetailAPIView.as_view(), 
            name='vehicle-detail'),

    path(   '<int:pk>/admin/', 
            views.ADMINVehicleDetailAPIView.as_view(), 
            name='admin-vehicle-detail'),

    path(   'create/', 
            views.VehicleCreateAPIView.as_view(), 
            name='vehicle-create'),
]
