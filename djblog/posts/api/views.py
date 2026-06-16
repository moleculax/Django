from urllib import request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#IMPORTO EL SERIALIZERS CREADO
from posts.api.serializers import PostSerializer
# IMPORTO VIEWSET
from rest_framework import viewsets
import posts
# TRAEMOS EL MODELO
from posts.models import Post

# ======== ESTO FUNCIONA PERFECTO LO COMENTO PORQUE USARE VIEWSET =================================
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()  # ← AGREGADO: requerido por ModelViewSet
    serializer_class = PostSerializer  # ← AGREGADO: requerido por ModelViewSet

    def list(self,request):
# ============= USAMOS SERIALIZERS  creado en serializers.py  PARA TRAER DATOS ====================
        posts = self.get_queryset()  # usar self.get_queryset()
        serializer = self.get_serializer(posts, many=True)  #  usar self.get_serializer()
        return Response(status=status.HTTP_200_OK, data=serializer.data)
# ======================== AQUI TRAIGO POR ID  PERO PUEDO TRAER POR TITLE, ETC ====================

    def retrieve(self, request,pk: int):
        post = PostSerializer(Post.objects.get(pk=pk))
        return Response(status=status.HTTP_200_OK, data=post.data)

# =================================================================================================

    # DEFINO PARA CREAR POST CON EL METODO POST
    def create(self,request):
# ===================   USAMOS SERIALIZERS PARA CREAR POST =======================================
        serializer = self.get_serializer(data=request.data)  # ← CORREGIDO: usar self.get_serializer() y request.data
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)  # ← CORREGIDO: usar self.perform_create()
        return Response(status=status.HTTP_201_CREATED, data=serializer.data)
# ================================================================================================


# ======== ESTO FUNCIONA PERFECTO LO COMENTO PORQUE USARE VIEWSET ===================================
# class PostAPIView(APIView):
#     def get(self,request):
# # ============= USAMOS SERIALIZERS  creado en serializers.py  PARA TRAER DATOS ====================
#         posts = Post.objects.all()
#         serializer = PostSerializer(posts, many=True)
#         return Response(status=status.HTTP_200_OK, data=serializer.data)
# # =================================================================================================
#
#     # DEFINO PARA CREAR POST CON EL METODO POST
#     def post(self,request):
# # ===================   USAMOS SERIALIZERS PARA CREAR POST =======================================
#         serializer = PostSerializer(data=request.POST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(status=status.HTTP_201_CREATED, data=serializer.data)
# # ================================================================================================