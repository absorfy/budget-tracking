from decimal import Decimal
from rest_framework import serializers
from wallets.models import Wallet
from .models import Transaction, Category


class TransactionSerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    wallet = serializers.PrimaryKeyRelatedField(
        queryset=Wallet.objects.all(),
        pk_field=serializers.CharField()
    )
    category = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        pk_field=serializers.CharField(),
        required=False,
        allow_null=True
    )

    class Meta:
        model = Transaction
        fields = [
            "id",
            "wallet",
            "category",
            "type",
            "amount",
            "description",
            "created_at",
        ]
        read_only_fields = ["id", "created_at"]


    def validate_amount(self, value: Decimal):
        if value is None or value <= 0:
            raise serializers.ValidationError("Amount must be > 0.")
        return value


    def validate(self, attrs):
        tx_type = attrs.get("type")
        amount = attrs.get("amount")
        wallet: Wallet = attrs.get("wallet")
        category: Category | None = attrs.get("category")

        if category and category.type != tx_type:
            raise serializers.ValidationError({"category": "Category type mismatch."})

        if tx_type == Transaction.EXPENSE and wallet and amount:
            if wallet.balance < amount:
                raise serializers.ValidationError({"amount": "Not enough balance."})

        return attrs
    

    def create(self, validated_data):
        tx_type = validated_data["type"]
        amount = validated_data["amount"]
        wallet = validated_data["wallet"]
        validated_data["currency"] = wallet.currency

        tx = Transaction.objects.create(**validated_data)

        if tx_type == Transaction.INCOME:
            wallet.balance += amount
        else:
            wallet.balance -= amount
        wallet.save()

        return tx
    

class CategorySerializer(serializers.ModelSerializer):
    id = serializers.CharField(read_only=True)

    class Meta:
        model = Category
        fields = ["id", "name", "type"]

    def validate(self, attrs):
        name = (attrs.get("name") or "").strip()
        ctype = attrs.get("type")

        qs = Category.objects.filter(name__iexact=name, type=ctype)
        if self.instance:
            qs = qs.exclude(pk=self.instance.pk)

        if qs.exists():
            raise serializers.ValidationError({"name": "Category with this name and type already exists."})

        attrs["name"] = name
        return attrs