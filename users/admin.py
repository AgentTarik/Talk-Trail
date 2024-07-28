from django.contrib import admin

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserProfile, Post


class UserProfileAdmin(UserAdmin):
    model = UserProfile
    list_display = ('username', 'email', 'is_staff', 'is_superuser')
    search_fields = ('username', 'email')
    readonly_fields = ('id',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'bio', 'profile_image')}),
        ('Permissions', {'fields': ('is_staff', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'is_staff', 'is_superuser')}
        ),
    )

    ordering = ('username',)


class PostAdmin(admin.ModelAdmin):
    list_display = ('content', 'user', 'created_at')
    list_filter = ('created_at', 'user')
    search_fields = ('content', 'user__username')

    ordering = ('-created_at',)


admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(Post, PostAdmin)