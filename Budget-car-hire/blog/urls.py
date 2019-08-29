from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog_list'),
    path('create/', views.ArticleCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.BlogDetailView.as_view(), name='blog_detail'),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.ArticleDeteleView.as_view(), name='blog_delete'),
    path('<int:pk>/comment', views.create_comment, name='add_blog_comment'),
    # path('comment/<int:pk>/edit', views.comment_edit, name='edit_blog_comment'),
    path('comment/<int:pk>/delete', views.comment_delete, name='delete_blog_comment'),
]

