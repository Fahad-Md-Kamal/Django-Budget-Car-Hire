from django.urls import path, include

from VehicleApp.category_api import views

urlpatterns =[
    path(   '', 
            views.VehicleCategoryListAPIView.as_view(), 
            name='vehicle-category-list'),

    path(   '<int:pk>/', 
            views.VehicleCategoryDetailAPIView.as_view(), 
            name='vehiclecategory-detail'),

    path(   'create/', 
            views.VehicleCategoryCreateAPIView.as_view(), 
            name='vehiclecategory-create'),
]
