from django.urls import path
from .views import TransactionListCreateView

urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view(), name="transactions-list-create"),
]