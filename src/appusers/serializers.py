from rest_framework import serializers
from django.conf import settings
from django.contrib.auth import get_user_model
from django.db.models import Q

User = get_user_model()


class UserPublicSerializer(serializers.ModelSerializer):
    """
    User Public Details serializer
    """
    password            = serializers.CharField(style={'input_type':'password'}, write_only=True)
    class Meta:
        model           = User
        fields          = ( 'id',
                            'url',
                            'username', 
                            'email', 
                            'password', 
                            'image')


class UserDetailSerializer(serializers.ModelSerializer):
    """
    User Details serializer
    """
    class Meta:
        model           = User
        fields          = ( 'id', 
                            'username', 
                            'email', 
                            'first_name', 
                            'last_name', 
                            'image')

        extra_kwargs = { "email":{ "read_only":True } }


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


class UserLoginSerializer(UserPublicSerializer):
    """
    User Login serializer
    """
    class Meta:
        model           = User
        fields          = ( 'username',
                            'email', 
                            'password')
        extra_kwargs = { "password":{ "write_only":True, "styel":"password" } }




# class UserLoginSerializer(UserPublicSerializer):
#     """
#     User Login serializer (Username or Email)
#     """
#     token               = serializers.CharField(read_only=True)
#     Identity            = serializers.CharField(label="Username/ Email")

#     class Meta:
#         model           = User
#         fields          = ( 'token',
#                             'Identity',
#                             'password')
#         extra_kwargs = {
#             "password":{
#                 "write_only":True,
#                 "styel":"password"
#             }
#         }

    # def validate(self, data):
    #     user_obj = None
    #     userid          = data.get('Identity', None)
    #     password        = data.get('password')
    #     if userid is None:
    #         raise ValueError("Username or Email is required to Login")
    #     user = User.objects.filter(
    #         Q(email=userid) |
    #         Q(username=userid))
    #     if user.exists() and user.count() == 1:
    #         user_obj = user.first()
    #         if user_obj:
    #             if not user_obj.check_password(password):
    #                 raise serializers.ValidationError("Invalid Login Credentials, Please Try again !")
    #     else:
    #         raise serializers.ValidationError("This not a registared Email/ Username")
        
    #     return data


