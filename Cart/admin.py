# Standard library import
from django.contrib import admin

# Local import
from .models import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    # list_display = ('user', 'product', 'created', 'quantity')
    # search_fields = ('product',)
    date_hierarchy = 'created'
    ordering = ('created',)