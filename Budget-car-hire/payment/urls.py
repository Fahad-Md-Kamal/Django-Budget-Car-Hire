from django.urls import path
from . import views

app_name='payment'


urlpatterns = [
    path('fleet/<int:pk>/', views.MakePayment.as_view(), name='make_payment' )
]