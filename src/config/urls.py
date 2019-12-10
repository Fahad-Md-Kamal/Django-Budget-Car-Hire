
from django.contrib import admin
from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('appusers.urls')),
    path('api/blog/', include('blogs.urls')),
    path('api/auth/', include('appusers.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
]


'''
curl -X POST -H "Content-Type: application/json" -d '{"email":"fahad@gmail.com","username":"fahad","password":"123"}' http://localhost:8000/api/auth/
curl -X POST -H "Content-Type: application/json" http://localhost:8000/api/blog/



curl -H "Authorization: JWT eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxLCJ1c2VybmFtZSI6ImZhaGFkIiwiZXhwIjoxNTc1OTAyNDc3LCJlbWFpbCI6ImZhaGFkQGdtYWlsLmNvbSIsIm9yaWdfaWF0IjoxNTc1OTAyMTc3fQ.sBIe7T-kT9ch7s86b4KDuCAg779iUuS7rGXcfMOhM6U" http://localhost:8000/api/blog/

'''