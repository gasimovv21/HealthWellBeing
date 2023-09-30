from rest_framework import serializers
from .models import TextMessage


class SendMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TextMessage
        fields = '__all__'