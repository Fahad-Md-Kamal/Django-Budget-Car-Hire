from django.contrib.auth import get_user_model
from rest_framework import generics
from appusers.auth import serializers

User = get_user_model()

class UserRegisterAPIView(generics.CreateAPIView):
    """
    CREATE user information
    """
    permission_classes          = []
    authentication_classes      = []
    queryset                    = User.objects.all()
    serializer_class            = serializers.UserRegisterSerializer

    def post(self, request, *args, **kwargs):
        """
        Handles post request to create users
        """
        return self.create(request, *args, **kwargs)
