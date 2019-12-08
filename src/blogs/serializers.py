from rest_framework import serializers

from appusers import serializers as User_serializer
from core.models import Blog

class BlogDetailSerializer(serializers.ModelSerializer):
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
        

class BlogListSerializer(BlogDetailSerializer):
    user          = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Blog
        fields = (
            'id', 
            'url',
            'title',
            'topic',
            'posted_on',
            'user',
        )
        