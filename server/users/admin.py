#server/users/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """Custom Admin configuration for User model"""
    
    list_display = [
        'username', 'email', 'full_name', 'user_type', 
        'is_verified', 'is_active', 'date_joined'
    ]
    
    list_filter = [
        'user_type', 'is_verified', 'is_active', 'is_staff', 
        'date_joined'
    ]
    
    search_fields = [
        'username', 'email', 'first_name', 'last_name', 
        'phone_number', 'agency_name'
    ]
    
    ordering = ['-date_joined']
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {
            'fields': (
                'first_name', 'last_name', 'email', 'phone_number',
                'profile_picture'
            )
        }),
        (_('Role and Status'), {
            'fields': (
                'user_type', 'is_verified', 'is_active', 'is_staff', 
                'is_superuser'
            )
        }),
        (_('Agent Information'), {
            'fields': (
                'license_number', 'agency_name', 'years_experience', 'bio'
            ),
            'classes': ('collapse',)  # Makes this section collapsible
        }),
        (_('Important dates'), {
            'fields': ('last_login', 'date_joined', 'updated_at')
        }),
        (_('Permissions'), {
            'fields': ('groups', 'user_permissions'),
        }),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'username', 'email', 'password1', 'password2',
                'first_name', 'last_name', 'phone_number', 'user_type'
            ),
        }),
    )
    
    readonly_fields = ['date_joined', 'updated_at']
    
    actions = ['approve_agents', 'deactivate_users']
    
    def approve_agents(self, request, queryset):
        """Admin action to approve selected agents"""
        agents = queryset.filter(user_type=User.UserType.AGENT, is_verified=False)
        updated = agents.update(is_verified=True)
        self.message_user(request, f'{updated} agents approved successfully.')
    approve_agents.short_description = _('Approve selected agents')
    
    def deactivate_users(self, request, queryset):
        """Admin action to deactivate selected users"""
        updated = queryset.update(is_active=False)
        self.message_user(request, f'{updated} users deactivated successfully.')
    deactivate_users.short_description = _('Deactivate selected users')
    
    def get_queryset(self, request):
        """Optimize queryset by selecting related fields"""
        return super().get_queryset(request).select_related()