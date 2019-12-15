from rest_framework import serializers

from AppUsers.serializers import UserListSerializer
from CoreApp.models import Comment, Blog
from StatusApp.Comment_api.serializers import CommentListSerializer


class BlogDetailSerializer(serializers.HyperlinkedModelSerializer):
    posted_on                   = serializers.ReadOnlyField(read_only=True)     
    updated_on                  = serializers.ReadOnlyField(read_only=True)
    blog_topic                  = serializers.SerializerMethodField(read_only=True)
    author                      = UserListSerializer(read_only=True)
    approved_by                 = UserListSerializer(read_only=True)
    replays                     = serializers.SerializerMethodField(read_only=True)
    
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
                                    'is_approved',
                                    'replays',
                                    'approved_by',
                                    'is_approved',)

        read_only_fields        = ('is_approved', )

    def get_blog_topic(self, obj):
        return obj.topic.topic
    
    def get_replays(self, obj):
        request                 = self.context.get('request')
        qs                      = Comment.objects.filter(blog=obj).order_by('-commented_on')
        data                    = { 'total-replays' : qs.count(),
                                    'replays': CommentListSerializer(qs, many=True, context={'request':request}).data 
                                    }
        return data


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
                                    'is_approved',
                                    'approved_by',)

    