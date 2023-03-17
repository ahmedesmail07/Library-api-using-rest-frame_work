from rest_framework import status
from django.urls import reverse
from rest_framework.test import APITestCase
from books.models import Book


class APITests(APITestCase):
    @classmethod
    def setUp(cls):
        cls.book = Book.objects.create(
            title="Fuck Every Thing",
            subtitle="I hate everybody",
            author="Ahmed Esmail",
            isbn="1234567890123",
        )

    def test_api_listview(self):
        response = self.client.get(reverse("book_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Book.objects.count(), 1)
        self.assertContains(response, self.book)
