from django.db import models

class Category(models.Model):
    name = models.CharField('name', max_length=255)
    description = models.CharField('description', max_length=255)

    def __str__(self):
        """Represent model object."""
        return f'{self.id:>2} {self.name} ({self.truncate_with_ellipsis(self.description)})'

    @staticmethod
    def truncate_with_ellipsis(text, max_length=30):
        """Truncate text to fit within max_length, adding ellipsis if needed."""
        if len(text) <= max_length:
            return text
        return f'{text[:max_length - 3]}...'
