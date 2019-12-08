
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('appusers.urls')),
    path('api/blog/', include('blogs.urls')),
    # path('api/auth/', obtain_jwt_token, name='user-token'),
    # path('api/token/refresh/', refresh_jwt_token, name='-refresh-user-token'),
]
