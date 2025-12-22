from rest_framework import generics
from .models import Transaction
from .serializers import TransactionSerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        qs = Transaction.objects.all().order_by("-created_at")

        wallet_id = self.request.query_params.get("wallet")
        if wallet_id:
            qs = qs.filter(wallet_id=wallet_id)

        return qs
