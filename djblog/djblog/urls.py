"""
URL configuration for djblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('',a Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

# from posts.views import HelloWorld
from home.views import HomeView
from nosotros.views import nosotros
# from posts.api.views import PostAPIView
# ESTO FUE CREADO EN router.py
from posts.api.router import router_post

urlpatterns = [
    path("admin/", admin.site.urls),
   # / path("posts/", HelloWorld.as_view()),
    path("nosotros/", nosotros.as_view()),
    # path("api/posts/", PostAPIView.as_view()),
    path('', HomeView.as_view(), name='home'),
    # AGREGO LAS RUTAS DE LOS VIEWSETS
    path('api/', include(router_post.urls)),

]




