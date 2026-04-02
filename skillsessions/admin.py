from django.contrib import admin
from .models import Session, SessionMembership, SessionMessage


@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('title', 'skill', 'host', 'date_time', 'capacity', 'created_at')
    readonly_fields = ('created_at', 'updated_at')


@admin.register(SessionMembership)
class SessionMembershipAdmin(admin.ModelAdmin):
    list_display = ('session', 'user', 'joined_at')
    readonly_fields = ('joined_at',)


@admin.register(SessionMessage)
class SessionMessageAdmin(admin.ModelAdmin):
    list_display = ('session', 'author', 'is_announcement', 'created_at', 'updated_at')
    list_filter = ('is_announcement', 'created_at')
    readonly_fields = ('created_at', 'updated_at')
