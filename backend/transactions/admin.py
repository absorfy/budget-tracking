from django.contrib import admin
from .models import Category, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "type")
    list_filter = ("type",)
    search_fields = ("name",)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ("id", "type", "amount", "wallet", "category", "created_at")
    list_filter = ("type", "created_at", "wallet")
    search_fields = ("description",)
    autocomplete_fields = ("wallet", "category")
    date_hierarchy = "created_at"
