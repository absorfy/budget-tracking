from rest_framework import serializers
from .models import Wallet
from currencies.models import Currency


class WalletSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    currency = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(),
        pk_field=serializers.CharField(),
        required=False,
        allow_null=True,
    )

    class Meta:
        model = Wallet
        fields = ("id", "name", "currency", "balance", "created_at", "updated_at")
        read_only_fields = ("id", "created_at", "updated_at")

    def create(self, validated_data):
        if "currency" not in validated_data or validated_data["currency"] is None:
            uah, _ = Currency.objects.get_or_create(code="UAH", defaults={"kind": "fiat", "name": "Ukrainian Hryvnia"})
            validated_data["currency"] = uah
        return super().create(validated_data)