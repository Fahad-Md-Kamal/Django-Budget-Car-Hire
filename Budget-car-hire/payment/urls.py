from django.urls import path
from . import views

app_name='payment'


urlpatterns = [
    path('', views.MakePayment.as_view(), name='pay' )
]