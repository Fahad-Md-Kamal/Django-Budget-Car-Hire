from django.urls import path
from django.core.exceptions import PermissionDenied
from . import views

def staff_user(function):
    def wrap(request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_staff:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    return wrap



app_name = 'blogs'

urlpatterns = [
    path('', views.ArticleListView.as_view(), name='blog_list'),
    path('admin-view/', views.AdminArticleView.as_view(), name='admin_blog_list'),
    path('create/', views.ArticleCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.ArticleDetailView.as_view(), name='blog_detail'),
    path('admin/<int:pk>/', views.AdminArticleDetail.as_view(), name='admins_blog_detail'),
    path('<int:pk>/update', views.ArticleUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.ArticleDeteleView.as_view(), name='blog_delete'),
    path('comment/<int:pk>/comment', views.create_comment, name='add_blog_comment'),
    path('comment/<int:pk>/delete', views.comment_delete, name='delete_blog_comment'),
]

