from django.db import migrations

from simple_blog.factories import ArticleFactory


def populate(apps, schema_editor):
    Article = apps.get_model("articles", "Article")

    class MigrationArticleFactory(ArticleFactory):
        class Meta:
            model = Article

    MigrationArticleFactory.create_batch(10)


class Migration(migrations.Migration):
    dependencies = [
        ("articles", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
