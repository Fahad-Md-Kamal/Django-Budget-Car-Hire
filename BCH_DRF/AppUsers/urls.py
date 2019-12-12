from django.urls import path

from AppUsers import views as user_views


urlpatterns =[
    path('', user_views.UsersListAPIView.as_view(), name='user-list'),
    path('create/', user_views.UserCreateAPIView.as_view(), name='user-create'),
    path('<int:pk>/', user_views.UserDetailAPIView.as_view(), name='user-detail'),
    path('<int:pk>/admin/', user_views.UserDetailAdminAPIView.as_view(), name='user-detail-Admin'),
    path('<int:pk>/staff/', user_views.UserDetailStaffAPIView.as_view(), name='user-detail-staff'),
]
