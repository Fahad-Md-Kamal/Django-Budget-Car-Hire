from rest_framework import serializers

from CoreApp.models import Comment
from AppUsers.serializers import UserInfoSerializer
from StatusApp.serializers import BlogListSerializer

class CommentListSerializer(serializers.HyperlinkedModelSerializer):
    user                    = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model               = Comment
        fields              = ( 'url', 
                                'text',
                                'commented_on',
                                'user')
    
    def get_user(self, obj):
        return obj.user.username


class CommentDetailSerializer(serializers.HyperlinkedModelSerializer):
    user                    = UserInfoSerializer(read_only=True)
    parent_comment          = serializers.SerializerMethodField(read_only=True)
    repalys                 = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model               = Comment
        fields              = ( 'id', 
                                'url', 
                                'text',
                                'commented_on',
                                'user',
                                'blog',
                                'repalys',
                                'parent_comment' )

    def get_repalys(self, obj):
        request             = self.context.get('request')
        qs                  = Comment.objects.filter(parent_comment=obj).order_by('-commented_on')
        return qs.count()

    def get_parent_comment(self, obj):
        request             = self.context.get('request')
        data                = {}
        qs                  = Comment.objects.filter(parent_comment=obj).order_by('-commented_on')
        data                = {
                                'total-replays':qs.count(),
                                'replays' : CommentListSerializer(qs, many=True, context={'request':request}).data
                                }
        return data
        