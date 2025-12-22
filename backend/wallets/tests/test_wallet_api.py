from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from currencies.models import Currency
from wallets.models import Wallet


class WalletApiTests(APITestCase):
    def test_create_wallet(self):
        url = reverse("wallets-list-create")
        payload = {"name": "Main", "balance": "100.00"}

        res = self.client.post(url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertIn("id", res.data)
        self.assertEqual(res.data["name"], "Main")

        uah = Currency.objects.get(code='UAH')
        self.assertEqual(res.data["currency"], str(uah.id))

    def _uah(self):
        return Currency.objects.get_or_create(code="UAH", defaults={"kind": "fiat"})[0]

    def test_list_wallets(self):
        uah = self._uah()
        Wallet.objects.create(name="W1", balance="10.00", currency=uah)
        Wallet.objects.create(name="W2", balance="20.00", currency=uah)

        url = reverse("wallets-list-create")
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(res.data, list))
        self.assertGreaterEqual(len(res.data), 2)


    def test_rename_wallet_patch(self):
        uah = self._uah()
        w = Wallet.objects.create(name="Old", balance="0.00", currency=uah)

        url = reverse("wallets-detail", kwargs={"pk": str(w.pk)})
        res = self.client.patch(url, {"name": "New"}, format="json")

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["name"], "New")

        w.refresh_from_db()
        self.assertEqual(w.name, "New")


    def test_delete_wallet(self):
        uah = self._uah()
        w = Wallet.objects.create(name="ToDelete", balance="0.00", currency=uah)

        url = reverse("wallets-detail", kwargs={"pk": str(w.pk)})
        res = self.client.delete(url)

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Wallet.objects.filter(pk=w.pk).exists())


    def test_wallet_not_found(self):
        url = reverse("wallets-detail", kwargs={"pk": "64b7f1f77c1a4b2a3c4d5e6f"})
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)
