from django.db import models
from django.db.models import Count


class TimestampedModel(models.Model):
    """An abstract model with a pair of timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class User(TimestampedModel):
    """A blog user."""

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)
    nickname = models.CharField(max_length=100, null=True)


class Tag(TimestampedModel):
    """A tag for the group of posts."""

    title = models.CharField(max_length=100)


class Post(TimestampedModel):
    """A blog post."""

    title = models.CharField(max_length=200)
    body = models.TextField()
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)


class PostComment(TimestampedModel):
    """A commentary to the blog post."""

    body = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    response_to = models.ForeignKey(
        'PostComment', on_delete=models.SET_NULL, null=True,
    )
    creator = models.ForeignKey(User, on_delete=models.CASCADE)


class PostLike(TimestampedModel):
    """A positive reaction to the blog post."""

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['post', 'creator']


# --- Аннотирование ----------------------------------------------------------

class Clip(models.Model):
    title = models.CharField(max_length=200)

    def like(self):
        ClipLike.objects.create(clip=self)

    def dislike(self):
        ClipDislike.objects.create(clip=self)

    @classmethod
    def rates_for(cls, *args):
        """
        Returns a tuple of integers (likes, dislikes)
        for the clip(s) filtered by provided args.
        """
        ratings = cls.objects.filter(title__in=args).annotate(
            like_count=Count('cliplike', distinct=True),
            dislike_count=Count('clipdislike', distinct=True)
        ).order_by('title')
        return [(e.like_count, e.dislike_count) for e in ratings]


# Обычно используют одну модель как для положительных реакций,
# так и для отрицательных. Однако в рамках этого упражнения
# две отдельные модели использовать удобнее. В реальных проектах
# такое тоже встречается, когда некое явление пользователю
# позволено оценить одновременно и положительно, и отрицательно.
class ClipLike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)


class ClipDislike(models.Model):
    clip = models.ForeignKey(Clip, on_delete=models.CASCADE)
