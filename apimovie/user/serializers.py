# user/serializers.py
from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=150,
        help_text="Nombre de usuario",
        required=True
    )
    password = serializers.CharField(
        max_length=128,
        help_text="Contraseña",
        write_only=True,
        required=True
    )