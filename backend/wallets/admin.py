from django.contrib import admin
from .models import Wallet

# Register your models here.

@admin.register(Wallet)
class WalletAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "currency", "balance", "created_at", "updated_at")
    search_fields = ("name",)
    list_filter = ("currency",)