"""Admin configuration for accounts app."""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile


@admin.register(UserProfile)
class UserProfileAdmin(UserAdmin):
    """Custom admin for UserProfile model."""

    list_display = (
        'email',
        'first_name',
        'last_name',
        'user_type',
        'rating',
        'email_verified',
        'phone_verified',
        'is_staff',
        'created_at',
    )
    list_filter = (
        'user_type',
        'email_verified',
        'phone_verified',
        'identity_verified',
        'is_staff',
        'is_superuser',
        'is_active',
        'created_at',
    )
    search_fields = (
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'city',
        'state',
    )
    ordering = ('-created_at',)
    
    fieldsets = (
        (None, {
            'fields': ('email', 'password', 'username')
        }),
        ('Personal Info', {
            'fields': (
                'first_name',
                'last_name',
                'phone_number',
                'date_of_birth',
                'profile_image',
                'about_me',
            )
        }),
        ('User Type & Role', {
            'fields': ('user_type', 'rating')
        }),
        ('Location', {
            'fields': (
                'address',
                'city',
                'state',
                'zip_code',
                'country',
                'address_latitude',
                'address_longitude',
                'current_latitude',
                'current_longitude',
                'last_location_update',
            )
        }),
        ('Payment Settings', {
            'fields': ('payment_method', 'payment_frequency')
        }),
        ('Social Auth', {
            'fields': ('google_id', 'apple_id', 'facebook_id'),
            'classes': ('collapse',)
        }),
        ('Verification', {
            'fields': ('email_verified', 'phone_verified', 'identity_verified')
        }),
        ('Related Settings', {
            'fields': (
                'work_preference_id',
                'notification_id',
                'emergency_contact_id',
            ),
            'classes': ('collapse',)
        }),
        ('Permissions', {
            'fields': (
                'is_active',
                'is_staff',
                'is_superuser',
                'groups',
                'user_permissions',
            ),
            'classes': ('collapse',)
        }),
        ('Important Dates', {
            'fields': ('started_at', 'last_login', 'date_joined', 'created_at', 'updated_at')
        }),
    )
    
    readonly_fields = ('created_at', 'updated_at', 'token_created_at', 'token_updated_at', 'date_joined')
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'username',
                'first_name',
                'last_name',
                'password1',
                'password2',
                'user_type',
            ),
        }),
    )
