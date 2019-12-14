from django.urls import path, include

from BlogApp.replay_api import views

urlpatterns =[
    path('create/', views.RepalyCreateAPIView.as_view(), name='replay'),
    path('<int:pk>/', views.RepalyDetailAPIView.as_view(), name='replay-detail'),
]
