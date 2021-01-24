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
    path('', views.blog_list, name='blog_list'),
    path('admin-view/', views.admin_blog_list, name='admin_blog_list'),
    path('create/', views.write_blog_view, name='blog_create'),
    path('<int:pk>/detail', views.blog_detail, name='blog_detail'),
    path('admin-view/<int:pk>/detail', views.admin_blog_detail, name='admins_blog_detail'),
    path('<int:pk>/update', views.blog_update_view, name='blog_update'),
    path('<int:pk>/delete', views.blog_delete, name='blog_delete'),
    path('<int:pk>/approve', views.blog_approval, name='blog_approval'),
    path('comment/<int:pk>/comment', views.create_comment, name='add_blog_comment'),
    path('comment/<int:pk>/delete', views.comment_delete, name='delete_blog_comment'),
    path('search/', views.search, name='search'),
    path('about-us/', views.about_us, name='about_us'),
]

