from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User

class LoginSerializer(serializers.Serializer):
    name = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        user = authenticate(name=data['name'], password=data['password'])
        if not user:
            raise serializers.ValidationError("Credenciais inválidas")
        data['user'] = user
        return data