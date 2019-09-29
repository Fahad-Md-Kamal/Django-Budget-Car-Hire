from django.urls import path
from . import views

app_name='payment'


urlpatterns = [
    path('fleet/<int:pk>/', views.checkout, name='checkout' )
]