from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm


class CustomUserAdmin(UserAdmin): 
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    model = CustomUser

    list_filter = ('email', 'username', 'is_active', 'is_staff') 
    list_display = ('email', 'username', 'date_joined', 'last_login') 
    ordering = ('-date_joined',)                    
    search_fields = ('email', 'username', 'first_name')  

    fieldsets = (
        (None, {'fields': ('email', 'username', 'first_name', 'last_name', 'password',)}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
        ('Personal', {'fields': ('about',)}),
    )       



    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_staff', 'is_active',)
            }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)