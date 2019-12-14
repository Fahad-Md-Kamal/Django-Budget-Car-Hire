from rest_framework import serializers

from CoreApp.models import Blog, Comment, Replay
from AppUsers.serializers import UserInfoSerializer


class ReplayCreateSerializer(serializers.HyperlinkedModelSerializer):
    user                = UserInfoSerializer(read_only=True)

    class Meta:
        model           = Replay
        fields          = ( 'url', 
                            'text', 
                            'replied_on', 
                            'updated_on', 
                            'user', 
                            'comment', 
                            'blog')
        extra_kwargs    = {
            'replied_on': {'read_only':True},
            'updated_on': {'read_only':True} }


class ReplaysDetailSerializer(ReplayCreateSerializer):

    class Meta:
        model           = Replay
        fields          = ( 'url', 
                            'text', 
                            'replied_on', 
                            'updated_on', 
                            'user', 
                            'comment', 
                            'blog')
        extra_kwargs    = {
            'replied_on': {'read_only':True},
            'updated_on': {'read_only':True} }

