from django.contrib import admin

from api.models import Item


@admin.register(Item)
class YourModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price',)
