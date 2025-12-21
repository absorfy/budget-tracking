from django.db import models

# Create your models here.

from django.db import models

class Wallet(models.Model):
    name = models.CharField(max_length=20)
    currency = models.CharField(max_length=3, default="UAH")
    balance = models.DecimalField(max_digits=18, decimal_places=2, default=0)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.name} ({self.currency})"
