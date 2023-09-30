from django.urls import path
from .views import post_message

urlpatterns = [
    path('send_message/', post_message, name='send-message'),
]
