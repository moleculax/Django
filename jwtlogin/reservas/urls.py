# ============================================
# ARCHIVO: reservas/urls.py
# ============================================
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, HabitacionViewSet, ReservaViewSet

router = DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='clientes')
router.register(r'habitaciones', HabitacionViewSet, basename='habitaciones')
router.register(r'reservas', ReservaViewSet, basename='reservas')

urlpatterns = [
    path('', include(router.urls)),
]