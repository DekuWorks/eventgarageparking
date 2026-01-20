# pylint: disable=no-member,line-too-long,missing-module-docstring,missing-final-newline,too-many-lines
"""User profile models for extended user information and authentication."""

import mimetypes

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import MinValueValidator, MaxValueValidator
from decimal import Decimal
from django.db import models
from django.utils import timezone

from Settings.models import EmergencyContact, Notification, WorkPreference


class UserProfileManager(BaseUserManager):
    """Custom user manager for UserProfile model with email as the unique identifier."""

    def create_user(self, email, password=None, username=None, **extra_fields):
        """Create and return a regular user with an email and password."""
        if not email:
            raise ValueError("The Email field must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, username=None, **extra_fields):
        """Create and return a superuser with an email and password."""
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(email, password, username, **extra_fields)


class UserProfile(AbstractUser):
    """Extended user profile to store refresh tokens and additional user info."""

    username = models.CharField(max_length=150, unique=True, null=True, blank=True)
    email = models.EmailField(unique=True)
    user_type = models.CharField(
        max_length=20,
        choices=[("customer", "Customer"), ("driver", "Driver"), ("valet", "Valet")],
        default="customer",
    )

    # Basic profile fields
    refresh_token = models.TextField(blank=True, null=True)
    token_created_at = models.DateTimeField(auto_now_add=True)
    token_updated_at = models.DateTimeField(auto_now=True)
    about_me = models.TextField(
        blank=True, null=True, help_text="User's bio or description about themselves"
    )
    started_at = models.DateTimeField(
        default=timezone.now, help_text="When the user first started using the platform"
    )

    # Payment preferences
    payment_method = models.CharField(
        max_length=20,
        choices=[
            ("card", "Credit/Debit Card"),
            ("bank", "Bank Account"),
            ("apple_pay", "Apple Pay"),
            ("google_pay", "Google Pay"),
        ],
        default="card",
    )

    payment_frequency = models.CharField(
        max_length=20,
        choices=[
            ("instant", "Instant"),
            ("weekly", "Weekly"),
            ("biweekly", "Bi-weekly"),
            ("monthly", "Monthly"),
        ],
        default="instant",
    )

    # Social authentication fields
    google_id = models.CharField(max_length=255, blank=True, null=True)
    apple_id = models.CharField(max_length=255, blank=True, null=True)
    facebook_id = models.CharField(max_length=255, blank=True, null=True)

    # Profile image (S3)
    profile_image = models.ImageField(
        upload_to="profile_images/",
        blank=True,
        null=True,
        help_text="Profile image stored in S3",
    )

    # Additional fields
    phone_number = models.CharField(max_length=20, blank=True, null=True, unique=True, db_index=True)
    date_of_birth = models.DateField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    zip_code = models.CharField(max_length=10, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True, default="US")
    
    # Geocoded address coordinates (reverse geocoded from address)
    address_latitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Latitude of the user's street address (reverse geocoded)",
        db_index=True,
    )
    address_longitude = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
        help_text="Longitude of the user's street address (reverse geocoded)",
        db_index=True,
    )
    
    # Current location coordinates (real-time GPS tracking)
    current_latitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        help_text="Current latitude coordinate (real-time GPS location)",
        db_index=True,
    )
    current_longitude = models.DecimalField(
        max_digits=10,
        decimal_places=7,
        blank=True,
        null=True,
        help_text="Current longitude coordinate (real-time GPS location)",
        db_index=True,
    )
    last_location_update = models.DateTimeField(
        null=True,
        blank=True,
        help_text="Timestamp of last location update",
    )

    # Related IDs
    work_preference_id = models.ForeignKey(
        WorkPreference,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="ID of the user's work preference settings",
    )
    notification_id = models.ForeignKey(
        Notification,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="ID of the user's notification settings",
    )
    emergency_contact_id = models.ForeignKey(
        EmergencyContact,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="ID of the user's emergency contact",
    )
    # TODO: Create FavoriteTeam model in a separate app
    # favorite_team_id = models.ForeignKey(
    #     "apps.FavoriteTeam",
    #     on_delete=models.SET_NULL,
    #     blank=True,
    #     null=True,
    #     help_text="ID of the user's favorite team settings",
    # )

    # Verification fields
    email_verified = models.BooleanField(default=False)
    phone_verified = models.BooleanField(default=False)
    identity_verified = models.BooleanField(default=False)

    # Rating field (1-5 stars, with 1 decimal place)
    rating = models.DecimalField(
        max_digits=3,
        decimal_places=1,
        blank=True,
        null=True,
        validators=[MinValueValidator(Decimal('1.0')), MaxValueValidator(Decimal('5.0'))],
        help_text="User rating from 1.0 to 5.0 stars (1 decimal place)",
        db_index=True,
    )

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserProfileManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email

    class Meta:
        """Meta options for the UserProfile model."""

        verbose_name = "User Profile"
        verbose_name_plural = "User Profiles"

    @property
    def primary_payment_method(self):
        """Get the primary payment method details from StripeCustomer."""
        try:
            if hasattr(self, 'stripe_customer') and self.stripe_customer:
                default_payment_method = self.stripe_customer.default_payment_method
                if default_payment_method:
                    return default_payment_method.display_name
                # Fallback to first available payment method
                first_payment_method = self.stripe_customer.payment_methods.filter(is_active=True).first()
                if first_payment_method:
                    return first_payment_method.display_name
        except Exception:
            pass
        return "No payment method set"

    @property
    def has_payment_method(self):
        """Check if user has any payment method configured."""
        try:
            if hasattr(self, 'stripe_customer') and self.stripe_customer:
                return self.stripe_customer.has_payment_methods
        except Exception:
            pass
        return False

    @property
    def has_external_account(self):
        """Check if user has any external account configured (for payouts)."""
        try:
            if hasattr(self, 'stripe_customer') and self.stripe_customer:
                return self.stripe_customer.has_external_accounts
        except Exception:
            pass
        return False

    @property
    def payment_methods(self):
        """Get all payment methods for this user."""
        try:
            if hasattr(self, 'stripe_customer') and self.stripe_customer:
                return self.stripe_customer.payment_methods.filter(is_active=True)
        except Exception:
            pass
        return []

    @property
    def external_accounts(self):
        """Get all external accounts for this user."""
        try:
            if hasattr(self, 'stripe_customer') and self.stripe_customer:
                return self.stripe_customer.external_accounts.filter(is_active=True)
        except Exception:
            pass
        return []
