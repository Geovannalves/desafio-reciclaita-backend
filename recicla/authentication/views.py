# autenticacao/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import LoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            return Response({'mensagem': 'Login bem-sucedido', 'name': user.name})
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
