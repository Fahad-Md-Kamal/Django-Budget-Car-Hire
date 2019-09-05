from django.urls import path
from . import views

app_name = 'fleets'

urlpatterns = [
    path('', views.FleetListView.as_view(), name='fleet_list'),
    path('admin-view/', views.AdminFleetListView.as_view(), name='admin_fleets'),
    path('<int:pk>/', views.FleetDetailView.as_view(), name='fleet_detail'),
    path('register/', views.FleetCreateView.as_view(), name='fleet_register'),
    path('<int:pk>/update', views.FleetUpdateView.as_view(), name='fleet_update'),
    path('<int:pk>/delete', views.FleetDeleteView.as_view(), name='fleet_delete'),
    path('<int:fleetpk>/add_fleet_car/<int:carpk>', views.add_fleet_car, name= 'add_fleet_car'),
]
