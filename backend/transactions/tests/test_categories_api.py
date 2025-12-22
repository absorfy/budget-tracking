from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from transactions.models import Category


class CategoryApiTests(APITestCase):
    def test_create_category(self):
        url = reverse("categories-list-create")
        payload = {"name": "Food", "type": Category.EXPENSE}

        res = self.client.post(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", res.data)
        self.assertEqual(res.data["name"], "Food")
        self.assertEqual(res.data["type"], Category.EXPENSE)

    def test_list_categories(self):
        Category.objects.create(name="Food", type=Category.EXPENSE)
        Category.objects.create(name="Salary", type=Category.INCOME)

        url = reverse("categories-list-create")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(res.data, list))
        self.assertGreaterEqual(len(res.data), 2)

    def test_filter_categories_by_type(self):
        Category.objects.create(name="Food", type=Category.EXPENSE)
        Category.objects.create(name="Salary", type=Category.INCOME)

        url = reverse("categories-list-create")
        res = self.client.get(url, {"type": Category.EXPENSE})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["type"], Category.EXPENSE)

    def test_patch_category(self):
        c = Category.objects.create(name="Old", type=Category.EXPENSE)

        url = reverse("categories-detail", kwargs={"pk": str(c.pk)})
        res = self.client.patch(url, {"name": "New"}, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], "New")

    def test_delete_category(self):
        c = Category.objects.create(name="ToDelete", type=Category.EXPENSE)

        url = reverse("categories-detail", kwargs={"pk": str(c.pk)})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Category.objects.filter(pk=c.pk).exists())
