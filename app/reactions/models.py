from django.db import models
from django.db.models import Count, Q

from common.models import CommonModel
from users.models import User
from videos.models import Video

# youtube: 좋아요(like), 싫어요(dislike), 제거(removelike)
class Reaction(CommonModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    
    # boolean : True, False, None
    # like = models.BooleanField(default=True)

    LIKE = 1
    DISLIKE = -1
    NO_REACTION = 0

    REACTION_CHOICES = (
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (NO_REACTION, 'No reaction')
    )

    reaction = models.IntegerField(
        choices=REACTION_CHOICES,
        default=NO_REACTION
    )

    # from django.db.models import Count, Q
    @staticmethod
    def get_video_reaction(video):
        reactions = Reaction.objects.filter(video=video).aggregate(
            likes_count = Count('pk', filter=Q(reaction=Reaction.LIKE)),
            dislikes_count = Count('pk', filter=Q(reaction=Reaction.DISLIKE)),
        )

        return reactions