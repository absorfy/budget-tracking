from rest_framework import generics
from .models import Wallet
from .serializers import WalletSerializer

class WalletListCreateView(generics.ListCreateAPIView):
    queryset = Wallet.objects.all().order_by("-created_at")
    serializer_class = WalletSerializer