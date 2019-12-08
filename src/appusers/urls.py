from django.urls import path, include

from appusers import views

# http://127.0.0.1:8000/api/user/1/
urlpatterns = [
    path('', views.UserListAPIView.as_view() , name='user-list'),
    path('register/', views.UserRegisterAPIView.as_view(), name='register-user'),
    path('<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),
    path('login/', views.UserLoginAPIView.as_view(), name='login-user'),
]
