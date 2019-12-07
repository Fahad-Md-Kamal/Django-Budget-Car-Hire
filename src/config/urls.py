
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('appusers.urls')),
    path('api/auth/', include('appusers.auth.urls')),
]
