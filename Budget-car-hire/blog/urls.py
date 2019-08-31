from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog_list'),
    path('create/', views.ArticleCreateView.as_view(), name='blog_create'),
    path('article/<int:pk>/', views.ArticleDetailView.as_view(), name='blog_detail'),
    path('article/<int:pk>/update', views.ArticleUpdateView.as_view(), name='blog_update'),
    path('article/<int:pk>/delete', views.ArticleDeteleView.as_view(), name='blog_delete'),
    path('article/<int:pk>/comment', views.create_comment, name='add_blog_comment'),
    # path('comment/<int:pk>/edit', views.comment_edit, name='edit_blog_comment'),
    path('comment/<int:pk>/delete', views.comment_delete, name='delete_blog_comment'),
]

