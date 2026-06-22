from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from drf_spectacular.utils import extend_schema, OpenApiResponse


class LoginView(APIView):
    permission_classes = [AllowAny]

    @extend_schema(
        request={
            'application/json': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string', 'description': 'Nombre de usuario'},
                    'password': {'type': 'string', 'description': 'Contraseña'},
                },
                'required': ['username', 'password']
            }
        },
        responses={
            200: OpenApiResponse(description='Login exitoso - Devuelve token JWT'),
            401: OpenApiResponse(description='Credenciales incorrectas'),
        }
    )
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'access': str(refresh.access_token),
                'refresh': str(refresh),
                'message': 'Login exitoso'
            }, status=status.HTTP_200_OK)
        else:
            return Response({
                'error': 'Usuario o contraseña incorrectos'
            }, status=status.HTTP_401_UNAUTHORIZED)