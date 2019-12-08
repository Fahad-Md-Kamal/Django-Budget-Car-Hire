from django.contrib.auth import get_user_model

from rest_framework import serializers

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    """
    User REGISTER serializer
    """
    password            = serializers.CharField(style={'input_type':'password'}, write_only=True)
    password2           = serializers.CharField(style={'input_type':'password'}, write_only=True)
    message             = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model           = User
        fields          = ( 'id',
                            'url',
                            'username',
                            'email',
                            'message',
                            'password', 
                            'password2')
    def get_message(self, data):
        return "Thank you for registering. Please verify your email before continuing"
    

    def validate(self, data):
        pw              = data.get('password')
        pw2             = data.get('password2')
        if pw != pw2:
            raise serializers.ValidationError('Passwords must match')
        return data

    def create (self, validated_data):
        user_obj        = User(
            username    = validated_data.get('username'),
            email       = validated_data.get('email'))
        user_obj.set_password(validated_data.get('password'))
        user_obj.is_active = False
        user_obj.save()
        return user_obj
