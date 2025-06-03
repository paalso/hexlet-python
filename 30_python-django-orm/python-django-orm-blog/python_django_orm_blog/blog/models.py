from django.db import models, transaction, IntegrityError
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

    def __str__(self):
        return f'Post {self.id}'


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

# --- Транзакции -------------------------------------------------------------


class Project(models.Model):
    name = models.CharField(max_length=200)

    @classmethod
    def reorganize(cls, assignments):
        all_worker_ids = Worker.objects.values_list('id', flat=True)
        project_ids = {pid for pid in assignments.values() if pid is not None}

        existing_project_ids = set(
            cls.objects.\
                filter(id__in=project_ids).\
                values_list('id', flat=True)
        )
        if project_ids != existing_project_ids:
            raise IntegrityError("One or more project IDs do not exist.")

        with transaction.atomic():
            for worker_id in all_worker_ids:
                new_project_id = assignments.get(worker_id)
                Worker.objects.filter(id=worker_id).\
                       update(project_id=new_project_id)


class Worker(models.Model):
    name = models.CharField(max_length=200)
    project = models.ForeignKey(
        Project,
        null=True,
        on_delete=models.SET_NULL,
    )


# --- Эффективное использование ORM ------------------------------------------

class Teacher(models.Model):
    name = models.CharField(max_length=100)


class Student(models.Model):
    name = models.CharField(max_length=100)


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name='courses')


