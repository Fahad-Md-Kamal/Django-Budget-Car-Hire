from rest_framework import serializers

from AppUsers.serializers import UserInfoSerializer
from CoreApp.models import Comment, Blog

class BlogDetailSerializer(serializers.HyperlinkedModelSerializer):
    posted_on                   = serializers.ReadOnlyField(read_only=True)     
    updated_on                  = serializers.ReadOnlyField(read_only=True)
    blog_topic                  = serializers.SerializerMethodField(read_only=True)
    author                      = UserInfoSerializer(read_only=True)
    approved_by                 = UserInfoSerializer(read_only=True)
    
    class Meta:
        model                   = Blog
        fields                  = ( 'url',
                                    'author', 
                                    'title',
                                    'content',
                                    'topic',
                                    'blog_topic',
                                    'posted_on',
                                    'updated_on',
                                    'approved_by',
                                    'is_approved',)

        read_only_fields        = ('is_approved', )

    def get_blog_topic(self, obj):
        return obj.topic.topic


class BlogListSerializer(BlogDetailSerializer):
    
    class Meta:
        model                   = Blog
        fields                  = ( 'url',
                                    'author', 
                                    'title',
                                    'blog_topic',
                                    'posted_on',)

class AdminBlogDetailSerializer(BlogDetailSerializer):
    
    class Meta:
        model                   = Blog
        fields                  = ( 'url',
                                    'author', 
                                    'title',
                                    'content',
                                    'topic',
                                    'blog_topic',
                                    'posted_on',
                                    'updated_on',
                                    'approved_by',
                                    'is_approved',)


    