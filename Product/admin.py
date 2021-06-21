# Standard library import
from django.contrib import admin

# Local import
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'available')
    list_filter = ('available',)
    search_fields = ('title', 'description')


admin.site.register(Product, ProductAdmin)