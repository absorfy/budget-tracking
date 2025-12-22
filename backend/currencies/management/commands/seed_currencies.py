from django.core.management.base import BaseCommand
from currencies.models import Currency


class Command(BaseCommand):
    help = "Seed base currencies (fiat + crypto)"

    def handle(self, *args, **options):
        currencies = [
            {"code": "UAH", "kind": Currency.FIAT, "name": "Ukrainian Hryvnia"},
            {"code": "USD", "kind": Currency.FIAT, "name": "US Dollar"},
            {"code": "EUR", "kind": Currency.FIAT, "name": "Euro"},

            {"code": "BTC", "kind": Currency.CRYPTO, "name": "Bitcoin"},
            {"code": "ETH", "kind": Currency.CRYPTO, "name": "Ethereum"},
        ]

        created = 0
        for data in currencies:
            _, was_created = Currency.objects.get_or_create(
                code=data["code"],
                defaults={
                    "kind": data["kind"],
                    "name": data["name"],
                },
            )
            if was_created:
                created += 1

        self.stdout.write(
            self.style.SUCCESS(f"Currencies seeded. New: {created}")
        )
