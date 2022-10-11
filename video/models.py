from django.db import models
from users.models import User
# Create your models here.

class Video(models.Model):
    title = models.CharField(max_length=255, unique=True)
    url = models.URLField(max_length = 255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    # likes = models.ManyToManyField(User, related_name="video_like")

    def get_total_likes(self):
        return self.like.user.count()

    def get_total_dislikes(self):
        return self.dislike.user.count()

    def __str__(self) -> str:
        return self.title

    # def get_obj(self):
    #     return self

class Like(models.Model):
    video = models.OneToOneField(Video, related_name="like", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="liked_user",)

    def __str__(self):
        return self.video.title

class Dislike(models.Model):
    video = models.OneToOneField(Video, related_name="dislike", on_delete=models.CASCADE)
    user = models.ManyToManyField(User, related_name="disliked_user",)

    def __str__(self):
        return self.video.title

    
