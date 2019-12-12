from rest_framework import serializers
from PIL import Image

from CoreApp import models
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


## BLOG Serializers
class BlogDetailSerializer(serializers.ModelSerializer):
    content             = serializers.CharField(required= False)
    user                = UserInfoSerializer(read_only= True)
    image               = serializers.ImageField(max_length=None, allow_empty_file=True, use_url=True)

    class Meta:
        model           = models.Blog
        fields          = ( 'id', 
                            'title', 
                            'content', 
                            'image', 
                            'posted_on', 
                            'updated_on', 
                            'is_approved', 
                            'user', 
                            'topic')

    def validate(self, data):
        content         = data.get('content', None)
        if content      == "":
            content     = None
        image           = data.get('image', None)
        
        if content is None and image is None:
            raise serializers.ValidationError('Image or content is required.')
        return data


class BlogListSerializer(serializers.ModelSerializer):

    class Meta:
        model           = models.Blog
        fields          = ( 'id', 
                            'url',
                            'title', 
                            'posted_on', 
                            'is_approved', 
                            'user', 
                            'topic')
