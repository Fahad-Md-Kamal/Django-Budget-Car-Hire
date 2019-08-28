from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog_list'),
    path('create/', views.ArticleCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
]

