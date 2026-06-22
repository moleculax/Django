from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

app_name = 'user'
urlpatterns = [
    # URL para iniciar sesión (genera el token)
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),

    # URL para refrescar el token cuando expire
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]