#server/users/models.py

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """
    Custom User model for HousePark Real Estate application.
    Extends Django's AbstractUser to add role-based functionality.
    """
    
    class UserType(models.TextChoices):
        BUYER = 'buyer', _('Property Buyer')
        AGENT = 'agent', _('Real Estate Agent')
        ADMIN = 'admin', _('Administrator')
    
    # Role and Basic Information
    user_type = models.CharField(
        _('user type'),
        max_length=10,
        choices=UserType.choices,
        default=UserType.BUYER,
        help_text=_('Designates the role of the user in the system')
    )
    
    phone_number = models.CharField(
        _('phone number'),
        max_length=15,
        blank=True,
        help_text=_('User\'s contact phone number')
    )
    
    # Verification and Status
    is_verified = models.BooleanField(
        _('verified status'),
        default=False,
        help_text=_('Designates whether the user has been verified. For agents, this means admin approval.')
    )
    
    # Agent-specific fields
    license_number = models.CharField(
        _('real estate license number'),
        max_length=50,
        blank=True,
        help_text=_('Official real estate license number for verified agents')
    )
    
    agency_name = models.CharField(
        _('agency name'),
        max_length=100,
        blank=True,
        help_text=_('Name of the real estate agency the agent works for')
    )
    
    years_experience = models.PositiveIntegerField(
        _('years of experience'),
        default=0,
        help_text=_('Number of years working in real estate industry')
    )
    
    bio = models.TextField(
        _('professional bio'),
        blank=True,
        help_text=_('Professional biography or description')
    )
    
    profile_picture = models.ImageField(
        _('profile picture'),
        upload_to='profile_pics/%Y/%m/%d/',
        blank=True,
        null=True,
        help_text=_('User profile picture')
    )
    
    # Timestamps
    date_joined = models.DateTimeField(
        _('date joined'),
        auto_now_add=True
    )
    
    updated_at = models.DateTimeField(
        _('updated at'),
        auto_now=True
    )
    
    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ['-date_joined']
        indexes = [
            models.Index(fields=['user_type', 'is_verified']),
            models.Index(fields=['date_joined']),
        ]
    
    def __str__(self):
        return f"{self.username} ({self.get_user_type_display()})"
    
    # Property-based role checkers for easy access
    @property
    def is_buyer(self):
        return self.user_type == self.UserType.BUYER
    
    @property
    def is_agent(self):
        return self.user_type == self.UserType.AGENT
    
    @property
    def is_administrator(self):
        return self.user_type == self.UserType.ADMIN
    
    @property
    def is_approved_agent(self):
        """Check if user is both an agent and verified/admin-approved"""
        return self.is_agent and self.is_verified
    
    @property
    def full_name(self):
        """Return the full name of the user"""
        return f"{self.first_name} {self.last_name}".strip()
    
    def save(self, *args, **kwargs):
        """Override save to handle role-based logic"""
        # Automatically set admin users as verified
        if self.is_administrator:
            self.is_verified = True
        
        # Ensure username is saved in lowercase for consistency
        if self.username:
            self.username = self.username.lower()
        
        super().save(*args, **kwargs)
