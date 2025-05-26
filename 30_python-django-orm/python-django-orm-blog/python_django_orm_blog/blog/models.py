from django.db import models


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


class CycleInGraphError(Exception):
    "An exception that means that some graph has cycles."


class Task(models.Model):
    value = models.CharField(max_length=200)
    parent = models.ForeignKey('self', null=True, on_delete=models.CASCADE)

    @property
    def root(self):
        "Returns a root task (task which parent is None)."
        # BEGIN (write your solution here)
        processed_ids = set()

        def root_searcher(task):
            parent_task = task.parent
            if parent_task is None:
                return task
            parent_task_id = parent_task.id
            if parent_task_id in processed_ids:
                raise CycleInGraphError(parent_task_id, f'Cyclic graph detected. Task {parent_task_id} has already been encountered')
            processed_ids.add(parent_task_id)
            return root_searcher(parent_task)

        return root_searcher(self)
        # END
