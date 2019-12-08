from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


# http://127.0.0.1:8000/api/user/1/
urlpatterns = [
    path('', obtain_jwt_token, name='user-auth'),
    path('refresher/', refresh_jwt_token, name='token-refresher'),
]
