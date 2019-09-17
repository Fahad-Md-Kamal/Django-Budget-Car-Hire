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
    path('', views.BlogListView.as_view(), name='blog_list'),
    path('admin-view/', views.admin_blog_list, name='admin_blog_list'),
    path('create/', views.BlogCreateView.as_view(), name='blog_create'),
    path('<int:pk>/', views.BlogDeteleView.as_view(), name='blog_detail'),
    path('admin-view/<int:pk>/', views.admin_blog_detail, name='admins_blog_detail'),
    path('<int:pk>/update', views.BlogUpdateView.as_view(), name='blog_update'),
    path('<int:pk>/delete', views.BlogDeteleView.as_view(), name='blog_delete'),
    path('comment/<int:pk>/comment', views.create_comment, name='add_blog_comment'),
    path('comment/<int:pk>/delete', views.comment_delete, name='delete_blog_comment'),
]

