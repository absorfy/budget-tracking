from django.contrib import admin
from .models import Currency


@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("id", "code", "kind", "name")
    list_filter = ("kind",)
    search_fields = ("code", "name")


# @admin.register(ExchangeRate)
# class ExchangeRateAdmin(admin.ModelAdmin):
#     list_display = ("id", "base", "quote", "rate", "date", "source")
#     list_filter = ("source", "date", "base", "quote")
#     search_fields = ("base__code", "quote__code", "source")
#     date_hierarchy = "date"
