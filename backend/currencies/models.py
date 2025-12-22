from django.db import models

class Currency(models.Model):
    FIAT = "fiat"
    CRYPTO = "crypto"
    KIND_CHOICES = [(FIAT, "Fiat"), (CRYPTO, "Crypto")]

    code = models.CharField(max_length=10, unique=True)
    kind = models.CharField(max_length=10, choices=KIND_CHOICES, default=FIAT)
    name = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return self.code


# class ExchangeRate(models.Model):
#     base = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_as_base")
#     quote = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="rates_as_quote")

#     rate = models.DecimalField(max_digits=20, decimal_places=10)
#     date = models.DateField()
#     source = models.CharField(max_length=32)

#     class Meta:
#         constraints = [
#             models.UniqueConstraint(fields=["base", "quote", "date", "source"], name="uniq_rate")
#         ]

#     def __str__(self):
#         return f"{self.base}->{self.quote} {self.rate} ({self.date})"
