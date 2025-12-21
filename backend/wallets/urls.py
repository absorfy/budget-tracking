from django.urls import path
from .views import WalletListCreateView, WalletDetailView

urlpatterns = [
    path("wallets/", WalletListCreateView.as_view(), name="wallets-list-create"),
    path("wallets/<str:pk>/", WalletDetailView.as_view(), name="wallets-detail"),
]
