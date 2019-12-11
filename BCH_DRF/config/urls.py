
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('AppUsers.auth.urls')),
    path('api/user/', include('CoreApp.urls')),
]
