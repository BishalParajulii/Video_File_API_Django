from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User , Video

class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ['email', 'name', 'phone_number', 'is_active', 'is_staff',  'user_type' ]# Ensure 'user_type' is correct
    ordering = ['email']
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'phone_number', 'user_type')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'name', 'phone_number', 'is_active', 'is_staff', 'user_type'),
        }),
    )

admin.site.register(User, CustomUserAdmin)


class VideoAdmin(admin.ModelAdmin):
    list_display = [ 'video_file', 'uploaded_at']
    list_filter = ['uploaded_at']

admin.site.register(Video, VideoAdmin)