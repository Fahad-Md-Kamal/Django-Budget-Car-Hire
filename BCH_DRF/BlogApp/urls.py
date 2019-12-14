from django.urls import path, include
from rest_framework.routers import DefaultRouter

from BlogApp import views


router      = DefaultRouter()

urlpatterns =[
    path('', views.BlogListAPIView.as_view(), name='blog-list'),
    path('create/', views.BlogCreationAPIView.as_view(), name='blog-create'),
    path('<int:pk>/', views.BlogDetailAPIView.as_view(), name='blog-detail'),path('<int:pk>/admin/', views.AdminBlogDetailAPIView.as_view(), name='blog-detail-admin'),
    path('topic/', views.BlogTopicListAPIView.as_view(), name='blog-category-list'),
    path('topic/create/', views.BlogTopicCreationAPIView.as_view(), name='blogtopic-create'),
    path('topic/<int:pk>/', views.BlogTopicDetailAPIView.as_view(), name='blogtopic-detail'),
    path('comment/', include('BlogApp.comment_api.urls')),
    path('repaly/', include('BlogApp.replay_api.urls')),
]
