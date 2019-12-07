from django.urls import path, include

from appusers import views


urlpatterns = [
    path('', views.UserListAPIView.as_view() , name='user-list'),
    path('<int:pk>/', views.UserDetailAPIView.as_view(), name='user-detail'),
]
