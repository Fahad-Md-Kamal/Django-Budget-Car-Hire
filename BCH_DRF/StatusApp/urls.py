from django.urls import path, include

from StatusApp import views

urlpatterns = [
    path('', views.BlogListAPIView.as_view(), name= 'blog-list'),
    path('create/', views.BlogCreationAPIView.as_view(), name= 'blog-create'),
    path('<int:pk>/', views.BlogDetailAPIView.as_view(), name= 'blog-detail'),
    path('<int:pk>/admin/', views.AdminBlogDetailAPIView.as_view(), name= 'admin-blog-detail'),
    path('topic/', include('StatusApp.BlogTopic_api.urls')),
    path('comment/', include('StatusApp.Comment_api.urls')),
]