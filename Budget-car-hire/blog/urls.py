from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog_list'),
    path('create/', views.ArticleCreateView.as_view(), name='article_create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='article_detail'),
]
