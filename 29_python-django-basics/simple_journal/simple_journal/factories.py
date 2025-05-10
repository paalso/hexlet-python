# simple_journal/factories.py

from django.utils import timezone
import factory
import factory.random
from simple_journal.articles.models import Article
from simple_journal.categories.models import Category

SEED = 4321

factory.random.reseed_random(SEED)


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Faker('word')
    description = factory.Faker('sentence', nb_words=4)


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    title = factory.Faker('text', max_nb_chars=50)
    content = factory.Faker('paragraph', nb_sentences=5, variable_nb_sentences=False)
    category = factory.SubFactory(CategoryFactory)
    pub_date = factory.Faker('date_time_this_decade', tzinfo=timezone.get_current_timezone())
