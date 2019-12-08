from rest_framework import serializers

from appusers import serializers as User_serializer
from core.models import Blog


class BlogAdminDetailSerializer(serializers.ModelSerializer):
    user          = User_serializer.UserPublicSerializer(read_only=True)
    blog_topic    = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id', 
            'title',
            'content',
            'topic',
            'blog_topic',
            'posted_on',
            'is_approved',
            'user',
        )

    def get_blog_topic(self, obj):
        return obj.get_topic_display()


class BlogCreateSerializer(serializers.ModelSerializer):
    user          = User_serializer.UserPublicSerializer(read_only=True)
    blog_topic    = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id', 
            'title',
            'content',
            'topic',
            'blog_topic',
            'posted_on',
            'user',
        )

    def get_blog_topic(self, obj):
        return obj.get_topic_display()

    def validate(self, data):
        title       = data.get('title')
        print(title)
        blog        = Blog.objects.filter( title   = title )
        if blog.exists():
            raise serializers.ValidationError("A blog with this title Already exists.")
        return data


class BlogPublicDetailSerializer(serializers.ModelSerializer):
    user          = User_serializer.UserPublicSerializer(read_only=True)
    blog_topic    = serializers.SerializerMethodField()

    class Meta:
        model = Blog
        fields = (
            'id', 
            'title',
            'content',
            'topic',
            'blog_topic',
            'posted_on',
            'user',
        )

    def get_blog_topic(self, obj):
        return obj.get_topic_display()
        

class BlogListSerializer(serializers.ModelSerializer):
    user          = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = (
            'id', 
            'url',
            'title',
            'posted_on',
            'user',
        )
        