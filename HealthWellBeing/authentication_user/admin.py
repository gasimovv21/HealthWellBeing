from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'phone_number',
        'date_of_birth',
        'username',
    ]
    search_fields = [
        'id',
        'phone_number',
        'date_of_birth',
        'username',
    ]
    list_filter = [
        'id',
        'phone_number',
        'date_of_birth',
        'username',
    ]
    empty_value_display = '-empty-'

