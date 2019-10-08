




##################         CONFIG APP



from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_view
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('register/', user_views.register, name= 'register'),
    path('profile/', user_views.profile, name= 'profile'),
    path('user-profile/<int:pk>/', user_views.user_detail, name='user_profile' ),
    path('login/', auth_view.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_view.LogoutView.as_view(template_name='index.html'), name='logout'),
    path('vehicle/', include('vehicle.urls', namespace='vehicle')),
    path('blogs/', include('blog.urls', namespace='blogs')),
    path('fleet/', include('fleet.urls', namespace='fleet')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)