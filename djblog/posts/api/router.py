from sys import prefix

# CREAMOS CUANDO USAMOS ViewSets
from rest_framework.routers import DefaultRouter
from posts.api.views import PostViewSet

router_post = DefaultRouter()
router_post.register(prefix='posts', viewset=PostViewSet, basename='post')