from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from .views import HomePage  # IMPORTAR HomePage (clase)


urlpatterns = [
    path("", HomePage.as_view(), name="home"),  # ← USAR .as_view()
    path("admin/", admin.site.urls),
    path("movie/", include("movie.urls")),
    path("user/", include("user.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]