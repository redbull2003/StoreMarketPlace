# Standard-library import
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from django.contrib import admin
from django.contrib import messages
from django.utils.translation import ngettext

# Local import
from .models import User, Profile
from .forms import UserCreationForm, UserChangeForm


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = (
        'username', 
        'email',
        'is_active', 
        'is_admin', 
        'is_superuser',
        'id',
    )
    list_display_links = ('username', 'email')
    list_filter = ('is_admin',)
    fieldsets = (
        ('user', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('is_active',)}),
        ('Permissions', {'fields': ('is_admin',)}),
        ('Admin_Perm', {'fields': ('is_superuser',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
    )
    search_fields = ('username',)
    ordering = ('username',)
    filter_horizontal = ()

    actions = ('add_to_admin', 'remove_from_admin')

    def add_to_admin(self, request, queryset):
        updated = queryset.update(is_admin=True)
        self.message_user(request, ngettext(
            '%d user was successfully add to admin.',
            '%d users were successfully add to admin.',
            updated,
        ) % updated, messages.SUCCESS)
    
    def remove_from_admin(self, request, queryset):
        updated = queryset.update(is_admin=False)
        self.message_user(request, ngettext(
            '%d user was successfully removed from admin.',
            '%d users were successfully removed from admin.',
            updated,
        ) % updated, messages.SUCCESS)


admin.site.register(User, UserAdmin)
admin.site.register(Profile)
admin.site.unregister(Group)
