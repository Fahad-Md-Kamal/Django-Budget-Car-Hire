from django.urls import path

from StatusApp.BlogTopic_api import views

urlpatterns = [
    path('', views.BlogTopicListAPIView.as_view(), name= 'blogtopic-list'),
    path('create/', views.BlogTopicCreateAPIView.as_view(), name= 'blogtopic-create'),
    path('<int:pk>/', views.BlogTopicRetrieveAPIView.as_view(), name= 'blogtopic-detail'),
]
