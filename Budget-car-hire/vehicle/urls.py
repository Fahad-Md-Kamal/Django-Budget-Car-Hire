from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
    path('', views.Vehicles_template_view.as_view(), name= 'index'),
    path('list/', views.VehicleListView.as_view(), name= 'vehicle_list'),
    path('admin-view/', views.AdminVehicleView.as_view(), name= 'admin_vehicle'),
    path('register/', views.VehicleRegisterView.as_view(), name= 'reg_vehicle'),
    path('<int:pk>/', views.VehicleDetaileView.as_view(), name= 'detail_vehicle'),
    path('<int:pk>/approve', views.approve_vehicle, name= 'approve_vehicle'),
    path('<int:pk>/freeze', views.freeze_vehicle, name= 'freeze_vehicle'),
    path('<int:pk>/update/', views.VehicleUpdateView.as_view(), name= 'update_vehicle'),
    path('<int:pk>/delete/', views.VehicleDeleteView.as_view(), name= 'delete_vehicle'),
]