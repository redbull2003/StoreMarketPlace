# Standard library import
from django.contrib import admin

# Local import
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'subject',
        'created',
        'show_body',
        'id',
    )
    search_fields = ('subject', 'show_body')