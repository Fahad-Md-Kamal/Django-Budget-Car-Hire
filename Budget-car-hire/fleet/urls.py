from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
       
    path(
        '',
        views.fleet_view, 
        name= 'fleets'),
       
    path(
        'detail/<int:pk>',
        views.fleet_detail_view, 
        name= 'detail_fleet'),
       
    path(
        'add-vehicle/<int:pk>',
        views.add_to_fleet, 
        name= 'add_to_fleet'),
       
    path(
        'existing-fleet/<int:pk>',
        views.existing_fleet, 
        name= 'existing_fleet'),

        ]