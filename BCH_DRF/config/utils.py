from AppUsers.serializers import UserInfoSerializer

def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': UserInfoSerializer(user, context={'request': request}).data
    }