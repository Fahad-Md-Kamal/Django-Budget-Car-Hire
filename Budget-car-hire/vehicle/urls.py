from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
       
    path('',
        views.vehicle_list_view, 
        name= 'vehicle_list'),
    
    path('admin-view/', 
        views.admin_vehicle_view, 
        name= 'admin_vehicle'),
    
    path('owner-view/', 
        views.owner_vehicle_list, 
        name= 'owner_vehicle_list'),
    
    path('search-vehicles/', 
        views.search_vehicle, 
        name= 'search_vehicle'),

    path('register/', 
        views.vehicle_registration, 
        name= 'reg_vehicle'),
    
    path('<int:pk>/', 
        views.vehicle_detail_view, 
        name= 'detail_vehicle'),
    
    path('<int:pk>/approve', 
        views.approve_vehicle, 
        name= 'approve_vehicle'),
    
    path('<int:pk>/freeze', 
        views.freeze_vehicle, 
        name= 'freeze_vehicle'),
    
    path('<int:pk>/update/', 
        views.vehicle_update_view, 
        name= 'update_vehicle'),
    
    path('<int:pk>/delete/', 
        views.vehicel_delete_view, 
        name= 'delete_vehicle'),
]