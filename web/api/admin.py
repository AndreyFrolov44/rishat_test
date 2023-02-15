from django.contrib import admin

from api.models import Item, Tax, Discount, Order


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id',)


@admin.register(Discount)
class DiscountAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'discount_amount',)


@admin.register(Tax)
class TaxAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'tax_amount',)
