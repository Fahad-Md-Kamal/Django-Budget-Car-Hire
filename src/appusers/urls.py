from django.urls import path, include

from appusers.views import UserDetailAPIView, UserListAPIView, UserCreateAPIView


urlpatterns = [
    path('', UserListAPIView.as_view() , name='user-list'),
    path('create/', UserCreateAPIView.as_view(), name='user-detail'),
    path('<int:pk>/', UserDetailAPIView.as_view(), name='user-detail'),
]
