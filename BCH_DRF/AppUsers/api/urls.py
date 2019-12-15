from django.urls import path

from AppUsers.api import views


urlpatterns =[
    path('', views.UserBlogListAPIView.as_view(), name='user-blog-list'),
]
