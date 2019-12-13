from rest_framework import serializers

from CoreApp.models import Comment
from AppUsers.serializers import UserInfoSerializer


class ParentCommentSerializer(serializers.ModelSerializer):
    user                = UserInfoSerializer(read_only=True)
    updated_on          = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model           = Comment
        fields          = ( 'id', 
                            'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'blog')


class ChildCommentSerializer(ParentCommentSerializer):
    blog                = serializers.ReadOnlyField(read_only=True)
    parent_comment      = ParentCommentSerializer(read_only=True)
    class Meta:
        model           = Comment
        fields          = ( 'id', 
                            'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'blog', 
                            'parent_comment')


class CommentDetailSerializer(ParentCommentSerializer):
    blog                = serializers.SerializerMethodField()

    class Meta:
        model           = Comment
        fields          = ( 'id', 
                            'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'blog')

    # def get_blog(self, data):
