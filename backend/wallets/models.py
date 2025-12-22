from django.db import models
from currencies.models import Currency

from django.db import models

class Wallet(models.Model):
    name = models.CharField(max_length=20)
    currency = currency = models.ForeignKey(
        Currency,
        on_delete=models.PROTECT,
        related_name="wallets",
    )
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.currency})"
