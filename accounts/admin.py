# admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'grade', 'points'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'grade', 'tags_interested')
        }),
        ('Events', {
            'fields': ('events_interested', 'events_participated')
        }),
        ('Points and Prizes', {
            'fields': ('points', 'coins', 'prizes_redeemed')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
                )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal Info', {
            'fields': ('first_name', 'last_name', 'email', 'grade', 'tags_interested')
        }),
        ('Events', {
            'fields': ('events_interested', 'events_participated')
        }),
        ('Points and Prizes', {
            'fields': ('points', 'coins', 'prizes_redeemed')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser'
                )
        }),
        ('Important Dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

admin.site.register(CustomUser, CustomUserAdmin)