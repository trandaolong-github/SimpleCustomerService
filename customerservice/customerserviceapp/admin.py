from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
# Register your models here.
from customerserviceapp.models import Ticket, CustomUser
from customerserviceapp.forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'is_staff', 'is_active', 'is_receiver', 'is_distributor')
    list_filter = ('username', 'is_staff', 'is_active', 'is_receiver', 'is_distributor')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_receiver', 'is_distributor')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active', 'is_receiver', 'is_distributor')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)

admin.site.register(Ticket)
