from django.urls import path, include

from VehicleApp.vehicleModel_api import views

urlpatterns =[
    path(   '', 
            views.VehicleModelListAPIView.as_view(), 
            name='vehicle-model-list'),

    path(   '<int:pk>/', 
            views.VehicleModelDetailAPIView.as_view(), 
            name='vehiclemodel-detail'),

    path(   'create/', 
            views.VehicleModelCreateAPIView.as_view(), 
            name='vehiclemodel-create'),
]
