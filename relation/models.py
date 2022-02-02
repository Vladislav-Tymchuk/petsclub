from django.db import models

from authentication.models import CustomUser
from mainPets.models import Comment, Post

class Followers(models.Model):

    followedPerson = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="Пользователь")
    followerPerson = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="Подписавшийся")

    class Meta:
        verbose_name_plural = "Followers"

    
    def __str__(self):
        id = str(self.id)
        return id


class LikePost(models.Model):

    likedPost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="Пост")
    likedPerson = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="Лайкнувший")

    class Meta:
        verbose_name_plural = "LikePosts"

    
    def __str__(self):

        id = str(self.id)
        return id


class LikeComment(models.Model):

    likedComment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="Комментарий")
    likedPerson = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING, related_name="Лайкнул")

    class Meta:
        verbose_name_plural = "LikeComments"

    
    def __str__(self):

        id = str(self.id)
        return id
