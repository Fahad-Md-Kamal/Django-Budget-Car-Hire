from django.urls import path
from . import views

app_name='payment'


urlpatterns = [
    path('fleet/<int:pk>/', views.make_payment, name='make_payment' )
]