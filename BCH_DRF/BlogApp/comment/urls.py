from django.urls import path, include

from BlogApp.comment import views

urlpatterns =[
    path('create/', views.ParentCommentCreateAPIView.as_view(), name='comment-create'),
    path('replay/', views.ChildCommentCreateAPIView.as_view(), name='comment-replay'),
    path('<int:pk>/', views.ParentCommentDetailAPIView.as_view(), name='comment-detail'),
]
