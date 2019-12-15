from django.urls import path, include

from StatusApp.Comment_api import views

urlpatterns = [
    path('', views.CommentListAPIView.as_view(), name= 'comment-list'),
    path('create/', views.CommentCreateAPIView.as_view(), name= 'comment'),
    path('<int:pk>/', views.CommentDetailAPIView.as_view(), name= 'comment-detail'),
]