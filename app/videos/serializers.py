from rest_framework import serializers
from .models import Video
from users.serializers import UserSerializer
from comments.serializers import CommentSerializer
from reactions.models import Reaction

class VideoSerializer(serializers.ModelSerializer):

    user = UserSerializer(read_only=True) # USER - VIDEO(FK)
    comment_set = CommentSerializer(many=True, read_only=True) # COMMENT(FK) - VIDEO
    # 부모가 자녀를 찾기 위해서 필요한 개념: Reverse Accessor => commnet

    # likes_count = serializers.IntegerField(read_only=True)
    # dislikes_count = serializers.IntegerField(read_only=True)

    reactions = serializers.SerializerMethodField()

    class Meta:
        model = Video
        fields = '__all__' # Video모델의 전체 필드를 보여줘
        # depth = 1

    def get_reactions(self, video):
        return Reaction.get_video_reaction(video)