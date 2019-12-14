from rest_framework import serializers

from CoreApp.models import Comment, Replay
from AppUsers.serializers import UserInfoSerializer
from BlogApp.replay_api.serializers import ReplaysDetailSerializer

class CommentCreateSerializer(serializers.HyperlinkedModelSerializer):
    user                = UserInfoSerializer(read_only=True)
    updated_on          = serializers.ReadOnlyField(read_only=True)

    class Meta:
        model           = Comment
        fields          = ( 'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'blog')

    def validate(self, data):
        blog            = data.get('blog', None)
        if blog is None:
            raise serializers.ValidationError('Corresponding Blog Post couldn\'t be found')
        return data


class CommentDetailSerializer(CommentCreateSerializer):
    replays             = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model           = Comment
        fields          = ( 'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'replays', 
                            'blog')
    
    def get_replays(self, obj):
        request     = self.context.get('request')
        qs              = Replay.objects.filter(comment_id=obj.id).order_by('-replied_on')[:10]
        data            = {
            'replay-count': qs.count(),
            'replays' : ReplaysDetailSerializer(qs, many=True, context={'request':request}).data,
        }
        return data


class CommentSerializer(CommentDetailSerializer):

    class Meta:
        model           = Comment
        fields          = ( 'url',
                            'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'replays')