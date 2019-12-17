from django.urls import path, include

from VehicleApp.vehiclePic_api import views

urlpatterns =[
    path('', views.VehiclePictureListAPIView.as_view(), name= 'vehicle-list'),
    path('<int:pk>/', views.VehiclePictureDetailAPIView.as_view(), name= 'vehiclepics-detail'),
    path('upload/', views.VehiclePictureUploadAPIView.as_view(), name= 'vehiclepics-upload'),
]
