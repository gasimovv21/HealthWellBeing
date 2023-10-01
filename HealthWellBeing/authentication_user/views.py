# authentication/views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login
from .models import CustomUser
from .serializers import UserSerializer
from django.contrib.auth.hashers import check_password

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        # Создаем пользователя, но не сохраняем его в базу данных
        user = serializer.save()
        
        # Устанавливаем is_active в True
        user.is_active = True
        user.save()

        # Возвращаем созданного пользователя
        return user

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = self.perform_create(serializer)
            return Response({'user_id': user.id, 'username': user.username}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(generics.GenericAPIView):
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username')
        password = request.data.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            user = None
        if user.password == password:
            login(request, user)
            return Response({'user_id': user.id, 'username': user.username})
        return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
