from django.urls import path
from . import views

app_name = 'fleets'

urlpatterns = [
    path('', views.FleetListView.as_view(), name='show_fleets'),
    path('admin-view/', views.AdminFleetListView.as_view(), name='admin_fleets'),
    path('<int:pk>/detail', views.FleetListView.as_view(), name='fleet_detail'),
    path('create/', views.FleetCreateView.as_view(), name='fleet_create'),
    path('<int:pk>/update', views.FleetUpdateView.as_view(), name='fleet_update'),
    path('<int:pk>/delete', views.FleetDeleteView.as_view(), name='fleet_delete'),
]

