import factory
from django.db import migrations
from simple_journal.factories import ArticleFactory


def populate(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')
    Article = apps.get_model('articles', 'Article')

    class MigrationArticleFactory(ArticleFactory):
        class Meta:
            model = Article
        category = factory.Iterator(Category.objects.all())

    MigrationArticleFactory.create_batch(30)


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
        ('categories', '0002_populate'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
