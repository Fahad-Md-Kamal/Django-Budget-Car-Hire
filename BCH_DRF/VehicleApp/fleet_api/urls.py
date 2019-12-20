from django.urls import path, include

from VehicleApp.fleet_api import views

urlpatterns =[
    path(   '', 
            views.FleetListAPIView.as_view(), 
            name='fleet-list'),
    path(   'create/', 
            views.FleetCreateAPIView.as_view(), 
            name='fleet-create'),
    path(   '<int:pk>/', 
            views.FleetDetailAPIView.as_view(), 
            name='fleet-detail'),
]
