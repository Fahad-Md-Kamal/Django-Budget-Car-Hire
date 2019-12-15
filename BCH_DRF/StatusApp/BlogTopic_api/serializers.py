from rest_framework import serializers

from CoreApp.models import BlogTopic
from AppUsers.serializers import UserListSerializer


class BlogTopicDetailSerializer(serializers.HyperlinkedModelSerializer):
    updated_on              = serializers.ReadOnlyField(read_only=True)
    created_by              = UserListSerializer(read_only=True)
    updated_by              = UserListSerializer(read_only=True)

    class Meta:
        model               = BlogTopic
        fields              = ( 'id',
                                'topic', 
                                'description', 
                                'updated_on', 
                                'created_by', 
                                'updated_by')


class BlogListSerializer(BlogTopicDetailSerializer):

    class Meta:
        model               = BlogTopic
        fields              = ( 'url',
                                'topic',)
                                
                                