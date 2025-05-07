from hexlet_django_blog.articles.models import Article
from django.test import TestCase
from django.urls import reverse


class ArticleTest(TestCase):
    def setUp(self):
        Article.objects.create(
            name="Как работает Django ORM",
            body="Django ORM (Object-Relational Mapping) — это абстракция,..."
        )
        Article.objects.create(
            name="Создание моделей в Django",
            body="Модели в Django описываются с помощью классов, где каждое..."
        )

    def test_articles_list(self):
        response = self.client.get(reverse("articles:articles_index"))
        self.assertEqual(response.status_code, 200)

        self.assertIn("articles", response.context)
        articles = response.context["articles"]

        # Проверяем не пустой ли список пользователей
        # print("Количество статей:", len(articles))
        self.assertTrue(len(articles) == 2)
