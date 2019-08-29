from django.urls import path
from . import views

app_name = 'vehicle'

urlpatterns = [
    path('', views.Vehicles_template_view.as_view(), name= 'index'),
]