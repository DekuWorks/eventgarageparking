"""Admin configuration for Settings app."""

from django.contrib import admin
from .models import EmergencyContact, Notification, WorkPreference


@admin.register(EmergencyContact)
class EmergencyContactAdmin(admin.ModelAdmin):
    """Admin for EmergencyContact model."""
    pass


@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    """Admin for Notification model."""
    pass


@admin.register(WorkPreference)
class WorkPreferenceAdmin(admin.ModelAdmin):
    """Admin for WorkPreference model."""
    pass
