from django.test import TestCase
from django.urls import reverse


class UsersTest(TestCase):
    def test_articles_list(self):
        response = self.client.get(reverse("articles:articles_index"))
        self.assertEqual(response.status_code, 200)
