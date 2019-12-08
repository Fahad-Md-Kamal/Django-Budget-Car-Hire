from django.urls import path, include
# from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from appusers.auth import views


urlpatterns = [
    path('', obtain_jwt_token, name='user-token'),
    path('register/', views.UserRegisterAPIView.as_view(), name='register-user'),
    path('token/refresh/', refresh_jwt_token, name='-refresh-user-token'),

]
