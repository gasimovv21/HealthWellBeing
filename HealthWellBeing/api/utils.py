import requests
import json
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from .serializers import SendMessageSerializer



def send_message(request):
    """
    |POST|=> Send message.
    """
    text_input = request.data.get('text')
    if not text_input:
        return Response({'Text': 'Message text does not exist.'}, status=status.HTTP_400_BAD_REQUEST)
    if len(text_input) > 0:
        data_for_serializer = {
            'text': text_input,
        }
        send_message_serializer = SendMessageSerializer(data=data_for_serializer)
        if send_message_serializer.is_valid():
            send_message_serializer.save()
            bearer_token = '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'
            headers = {
                'Authorization': f'Bearer {bearer_token}',
            }
            post_data = {
                "model": "text-davinci-003",
                "prompt": f"{text_input}",
                "max_tokens": 500,
                "temperature": 0.5
            }
            response = requests.post('https://api.openai.com/v1/completions', headers=headers, json=post_data)
            content = response.content
            data=json.loads(content)
            answer_from_bot = data["choices"][0]["text"].replace('\n', '')
            return Response(answer_from_bot, status=status.HTTP_201_CREATED)
        return Response(send_message_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response({'error': 'The length of message is low than 0.'}, status=status.HTTP_403_FORBIDDEN)