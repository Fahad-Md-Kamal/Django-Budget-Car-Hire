
from appusers import serializers

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': serializers.UserLoginSerializer(user, context={'request': request}).data
    }