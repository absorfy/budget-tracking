from django.urls import path
from .views import TransactionListCreateView, CategoryListCreateView, CategoryDetailView

urlpatterns = [
    path("transactions/", TransactionListCreateView.as_view(), name="transactions-list-create"),
    path("categories/", CategoryListCreateView.as_view(), name="categories-list-create"),
    path("categories/<str:pk>/", CategoryDetailView.as_view(), name="categories-detail"),
]