from django.contrib import admin
from django.urls import path , include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
     path('api-auth/', include('rest_framework.urls')),
    path('api/auth/', include('AppUsers.auth.urls')),
    path('api/user/', include('AppUsers.urls')),
    path('api/blog/', include('BlogApp.urls')),
    path('api/all/', include('AppUsers.api.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
