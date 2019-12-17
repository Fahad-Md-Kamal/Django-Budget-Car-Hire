from django.urls import path

from AppUsers.api import views


urlpatterns =[
    path('blogs/', views.UserBlogListAPIView.as_view(), name='user-blog-list'),
    path('vehicles/', views.UserVehicleListAPIView.as_view(), name='user-vehicle-list'),
]
