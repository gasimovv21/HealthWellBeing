from django.contrib import admin
from .models import TextMessage


@admin.register(TextMessage)
class TextMessageAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'text'
    ]
    search_fields = [
        'id',
        'text',
    ]
    list_filter = [
        'id',
        'text',
    ]

    empty_value_display = '-empty-'