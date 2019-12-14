from django.urls import path, include

from BlogApp.comment import views

urlpatterns =[
    path('<int:pk>/', views.CommentDetailAPIView.as_view(), name='comment-detail'),
    path('create/', views.CommentCreateAPIView.as_view(), name='comment'),
    ]
