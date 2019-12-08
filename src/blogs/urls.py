from django.urls import path, include

from blogs import views

# http://127.0.0.1:8000/api/blog/1
urlpatterns = [
    path('', views.BlogsListAPIView.as_view(), name='blog-list'),
    path('<int:pk>/', views.BlogsDetailAPIView.as_view(), name='blog-detail'),
    path('create/', views.BlogCreateAPIView.as_view(), name='blog-create'),
]
