from rest_framework import serializers

from CoreApp.models import Comment, Replay
from AppUsers.serializers import UserInfoSerializer

#    text                    = models.TextField(max_length=300)
#     replaied_on             = models.DateTimeField(auto_now_add=True)
#     updated_on              = models.DateTimeField(blank=True, null=True)
#     user                    = models.ForeignKey(AppUser, 
#                                 on_delete = models.SET_NULL, 
#                                 related_name= 'commenter_replayer',
#                                 blank=True, null=True)
#     comment                 = models.ForeignKey( Comment, 
#                                 on_delete = models.SET_NULL, 
#                                 blank=True, null=True)

class ReplaysSerializer(serializers.HyperlinkedModelSerializer):
    user                = UserInfoSerializer(read_only=True)

    class Meta:
        model           = Replay
        fields          = ( 'id', 
                            # 'url', 
                            'text', 
                            'replaied_on', 
                            'updated_on', 
                            'user')
        extra_kwargs    = {
            'replaied_on': {'read_only':True},
            'updated_on': {'read_only':True},
        }




class CommentCreateSerializer(serializers.ModelSerializer):
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

    def validate(self, data):
        blog            = data.get('blog', None)
        if blog is None:
            raise serializers.ValidationError('Corresponding Blog Post couldn\'t be found')
        return data


class CommentDetailSerializer(CommentCreateSerializer):
    # replays             = serializers.SerializerMethodField(read_only=True)


    class Meta:
        model           = Comment
        fields          = ( 'id', 
                            'url',
                            # 'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            # 'replays',
                            'blog')


class CommentSerializer(CommentCreateSerializer):
    replay              = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model           = Comment
        fields          = ( 'id', 
                            'url',
                            # 'content', 
                            'commented_on', 
                            'updated_on', 
                            'user', 
                            'replay'
                            )
    
    def get_replay(self, obj):
        request     = self.context.get('request')
        qs          = Replay.objects.filter(comment_id=obj.id).order_by('-replaied_on')[:10]
        data        = { 'replays': CommentSerializer(qs, many=True, context={'request':request}).data }
        return data