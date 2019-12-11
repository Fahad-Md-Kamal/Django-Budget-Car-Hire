from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token

urlpatterns = [
    path('', obtain_jwt_token, name='auth-token'),
    path('verify/token/', verify_jwt_token, name='verify-token'),
]
