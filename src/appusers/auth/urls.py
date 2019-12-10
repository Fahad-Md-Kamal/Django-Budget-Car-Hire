from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token
# from appusers.auth import views

# http://127.0.0.1:8000/api/user/1/
urlpatterns = [
    path('', obtain_jwt_token, name='user-auth'),
    # path('', views.AuthAPIView.as_view(), name='user-auth'),
    path('refresher/', refresh_jwt_token, name='token-refresher'),
]
