from django.shortcuts import get_object_or_404
from rest_framework import serializers
from PIL import Image

from CoreApp import models
from BlogApp.comment.serializers import CommentSerializer
from AppUsers.serializers import UserInfoSerializer


## BLOG CATEGORY Serializers
class BlogCategoryDetailSerializer(serializers.ModelSerializer):
    created_by           = UserInfoSerializer(read_only=True)
    updated_by          = UserInfoSerializer(read_only=True)

    class Meta:
        model           = models.BlogTopic
        fields          = ( 'id', 
                            'topic', 
                            'description', 
                            'created_by',
                            'created_on',
                            'updated_by',
                            'updated_on')


class BlogCategoryListSerializer(BlogCategoryDetailSerializer):

    class Meta:
        model           = models.BlogTopic
        fields          = ( 'id', 
                            'url',
                            'topic',)


class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model           = models.BlogTopic
        fields          = ( 'topic', )


# ## BLOG Serializers
class BlogDetailSerializer(serializers.ModelSerializer):
    content             = serializers.CharField(required= False)
    author              = UserInfoSerializer(read_only= True)
    blog_topic          = serializers.SerializerMethodField(read_only=True)
    updated_on          = serializers.ReadOnlyField(read_only=True)
    comments             = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model           = models.Blog
        fields          = ( 'id', 
                            'title', 
                            'content', 
                            'image', 
                            'posted_on', 
                            'updated_on', 
                            'author', 
                            'blog_topic' ,
                            'topic', 
                            'comments')

    def validate(self, data):
        content         = data.get('content', None)
        topic           = data.get('topic', None)
        if content      == "":
            content     = None
        image           = data.get('image', None)
        if content is None and image is None:
            raise serializers.ValidationError('Image or content is required.')
        if topic is None:
            raise serializers.ValidationError('Please Choose a topic for the blog')
        return data
    
    def get_blog_topic(self, obj):
        return obj.topic.topic
    
    def get_comments(self, obj):
        request     = self.context.get('request')
        qs          = models.Comment.objects.filter(blog=obj).order_by('-commented_on')[:10]
        data        = { 'comments': CommentSerializer(qs, many=True, context={'request':request}).data }
        return data



class AdminBlogDetailSerializer(BlogDetailSerializer):

    class Meta:
        model           = models.Blog
        fields          = ( 'id', 
                            'title', 
                            'content', 
                            'image', 
                            'posted_on', 
                            'updated_on', 
                            'approved_by',
                            'is_approved', 
                            'author', 
                            'blog_topic' ,
                            'topic')
        extra_kwargs    = { 'approved_by':{'read_only':True} }
        

class BlogListSerializer(BlogDetailSerializer):

    class Meta:
        model           = models.Blog
        fields          = ( 'id', 
                            'url',
                            'title', 
                            'posted_on', 
                            'is_approved', 
                            'author', 
                            'blog_topic')
