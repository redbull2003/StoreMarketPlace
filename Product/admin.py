# Standard library import
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

# Local import
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'unit_price',
        'amount',
        'discount',
        'total_price',
        'available',
        'created',
        'updated',
        'sell',
        'image_thumbnail',
    )
    list_filter = ('available',)
    search_fields = ('title', 'description')
    date_hierarchy = 'created'
    ordering = ('-sell',)
    empty_value_display = '???'
    list_editable = ('unit_price', 'discount', 'total_price')

    actions = ('make_available', 'make_unavailable')

    def make_available(self, request, queryset):
        updated = queryset.update(available=True)
        self.message_user(request, ngettext(
            '%d product was successfully marked as available.',
            '%d products were successfully marked as available.',
            updated,
        ) % updated, messages.SUCCESS)
    
    def make_unavailable(self, request, queryset):
        updated = queryset.update(available=False)
        self.message_user(request, ngettext(
            '%d product was successfully marked as unavailable.',
            '%d products were successfully marked as unavailable.',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(Product, ProductAdmin)