from rest_framework import generics
from .models import Transaction, Category
from .serializers import TransactionSerializer, CategorySerializer


class TransactionListCreateView(generics.ListCreateAPIView):
    serializer_class = TransactionSerializer

    def get_queryset(self):
        qs = Transaction.objects.all().order_by("-created_at")
        
        wallet_id = self.request.query_params.get("wallet")
        if wallet_id:
            qs = qs.filter(wallet_id=wallet_id)

        return qs
    

class TransactionDetailView(generics.RetrieveDestroyAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_destroy(self, instance: Transaction):
        wallet = instance.wallet
        if instance.type == Transaction.INCOME:
            wallet.balance -= instance.amount
        else:
            wallet.balance += instance.amount
        wallet.save()
        instance.delete()


class CategoryListCreateView(generics.ListCreateAPIView):
    serializer_class = CategorySerializer

    def get_queryset(self):
        qs = Category.objects.all().order_by("type", "name")
        t = self.request.query_params.get("type")
        if t:
            qs = qs.filter(type=t)
        return qs


class CategoryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
