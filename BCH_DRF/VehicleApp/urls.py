from django.urls import path, include

# from VehicleApp.category_api import views

urlpatterns =[
    path('', include('VehicleApp.vehicle_api.urls')),
    path('category/', include('VehicleApp.category_api.urls')),
    path('model/', include('VehicleApp.vehicleModel_api.urls')),
    path('image/', include('VehicleApp.vehiclePic_api.urls')),
]
