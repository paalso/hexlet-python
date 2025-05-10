from django.db import migrations
from simple_journal.factories import CategoryFactory


def populate(apps, schema_editor):
    Category = apps.get_model('categories', 'Category')

    class MigrationCategoryFactory(CategoryFactory):
        class Meta:
            model = Category
    MigrationCategoryFactory.create_batch(5)


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate),
    ]
