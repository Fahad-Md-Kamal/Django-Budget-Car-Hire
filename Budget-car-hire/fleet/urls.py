from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
       
    path(
        '',
        views.fleet_view,
        name= 'fleets'),

    path(
        'admin-view/',
        views.admin_fleet_view,
        name= 'admin_fleet_view'),
       
    path(
        'detail/<int:pk>/',
        views.fleet_detail_view,
        name= 'detail_fleet'),
       
    path(
        'detail/<int:pk>/<int:car_pk>',
        views.fleet_detail_view,
        name= 'detail_fleet'),
       
    path(
        'add-vehicle/<int:pk>',
        views.add_to_fleet,
        name= 'add_to_fleet'),
       
    path(
        'new-fleet/',
        views.new_fleet,
        name= 'new_fleet'),
       
    path(
        'existing-fleet/<int:pk>/',
        views.existing_fleet,
        name= 'existing_fleet'),
        
    path(
        'remove-vehicle/<int:fleet_pk>/<int:vehicle_pk>',
        views.remove_from_fleet,
        name= 'remove_from_fleet'),
        
    path(
        'cancel-fleet/<int:pk>/',
        views.cancel_fleet,
        name= 'cancel_fleet'),
        
    path(
        'remove-fleet/<int:pk>/',
        views.remove_fleet,
        name= 'remove_fleet'),
        
    path(
        'approve-fleet/<int:pk>/',
        views.approve_fleet,
        name= 'approve_fleet'),
        
    path(
        'freeze-fleet/<int:pk>/',
        views.freeze_fleet,
        name= 'freeze_fleet'),

    path(
        '<int:pk>/', 
        views.checkout, 
        name='checkout' ),

    path(
        'update_record/<int:pk>/<str:token>', 
        views.update_payment_record, 
        name='update_record' ),

        
]