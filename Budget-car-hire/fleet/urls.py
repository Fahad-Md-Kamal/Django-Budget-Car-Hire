from django.urls import path
from . import views

app_name = 'fleet'

urlpatterns = [
       
    path('',
        views.fleet_home, 
        name= 'fleet_home')
        ]