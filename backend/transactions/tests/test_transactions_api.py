from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse

from wallets.models import Wallet
from transactions.models import Transaction, Category


class TransactionApiTests(APITestCase):
    def setUp(self):
        self.wallet = Wallet.objects.create(name="Main", balance="100.00")

        self.cat_food = Category.objects.create(name="Food", type=Category.EXPENSE)
        self.cat_salary = Category.objects.create(name="Salary", type=Category.INCOME)

        self.url = reverse("transactions-list-create")


    def test_create_income_updates_wallet_balance(self):
        payload = {
            "wallet": str(self.wallet.id),
            "type": Transaction.INCOME,
            "amount": "50.00",
            "category": str(self.cat_salary.id),
            "description": "Salary",
        }

        res = self.client.post(self.url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.wallet.refresh_from_db()
        self.assertEqual(str(self.wallet.balance), "150.00")

    def test_create_expense_updates_wallet_balance(self):
        payload = {
            "wallet": str(self.wallet.id),
            "type": Transaction.EXPENSE,
            "amount": "30.00",
            "category": str(self.cat_food.id),
            "description": "Groceries",
        }

        res = self.client.post(self.url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.wallet.refresh_from_db()
        self.assertEqual(str(self.wallet.balance), "70.00")

    def test_create_expense_not_enough_balance_returns_400(self):
        payload = {
            "wallet": str(self.wallet.id),
            "type": Transaction.EXPENSE,
            "amount": "999.00",
            "category": str(self.cat_food.id),
        }

        res = self.client.post(self.url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

        self.wallet.refresh_from_db()
        self.assertEqual(str(self.wallet.balance), "100.00")  # не змінився

    def test_category_type_mismatch_returns_400(self):
        payload = {
            "wallet": str(self.wallet.id),
            "type": Transaction.EXPENSE,
            "amount": "10.00",
            "category": str(self.cat_salary.id),  # income category для expense
        }

        res = self.client.post(self.url, payload, format="json")

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_list_transactions_returns_list(self):
        Transaction.objects.create(
            wallet=self.wallet,
            type=Transaction.INCOME,
            amount="10.00",
            category=self.cat_salary,
        )
        Transaction.objects.create(
            wallet=self.wallet,
            type=Transaction.EXPENSE,
            amount="5.00",
            category=self.cat_food,
        )

        res = self.client.get(self.url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(isinstance(res.data, list))
        self.assertEqual(len(res.data), 2)

    def test_list_transactions_filter_by_wallet(self):
        w2 = Wallet.objects.create(name="Second", balance="0.00")

        Transaction.objects.create(wallet=self.wallet, type=Transaction.INCOME, amount="10.00")
        Transaction.objects.create(wallet=w2, type=Transaction.INCOME, amount="20.00")

        res = self.client.get(self.url, {"wallet": str(self.wallet.id)})

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]["wallet"], str(self.wallet.id))
