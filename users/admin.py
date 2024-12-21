from django.contrib import admin
from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'last_name', 'first_name', 'role', 'is_active')
    list_filter = ('id', 'last_name',)
    ordering = ('id',)
