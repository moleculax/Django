from urllib import request

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
#IMPORTO EL SERIALIZERS CREADO
from posts.api.serializers import PostSerializer
# IMPORTO VIEWSET
from rest_framework import viewsets
from rest_framework.decorators import action
import posts
# TRAEMOS EL MODELO
from posts.models import Post
# PARA AGREGAR PERMISOS A SOLO LOS LOGEADOS
from rest_framework.permissions import IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from posts.api.permissions import IsAdminOrReadOnly
# =========================================================
# ============ ESTO PERMITE CREAR EL CRUD COMPLETO ======================
class PostModelViewSet(viewsets.ModelViewSet):
    # permission_classes = (IsAuthenticated)
# ======AQUI PODEMOS AGREGAR VARIOS PERMISOS DESPUES DE LA (,) ==========
    permission_classes = [IsAdminOrReadOnly,]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
# ======================================================================
# ======================== RUTA PERSONALIZADA PARA BUSCAR POR TÍTULO ===============================
#     http: // localhost: 8000 / api / posts / title / Que % 20es % 20Django /
    @action(detail=False, methods=['get'], url_path='title/(?P<title>.+)')
    def retrieve_by_title(self, request, title=None):
        try:
            post = Post.objects.get(title=title)
            serializer = self.get_serializer(post)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Post.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'error': 'Post no encontrado'}
            )



# COMENTE TODO ESTO PORQUE USARE MODELVIEWSET
""" 
# ======== ESTO FUNCIONA PERFECTO LO COMENTO PORQUE USARE VIEWSET =================================
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def list(self, request):
# ============= USAMOS SERIALIZERS  creado en serializers.py  PARA TRAER DATOS ====================
        posts = self.get_queryset()
        serializer = self.get_serializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

# ======================== AQUI TRAIGO POR ID  PERO PUEDO TRAER POR TITLE, ETC ====================
# LE INDICO QUE TRAIGA POR ID USANDO pk
    def retrieve(self, request, pk: int):
        post = Post.objects.get(pk=pk)
        serializer = self.get_serializer(post)  # ← CORREGIDO
        return Response(status=status.HTTP_200_OK, data=serializer.data)

# ======================== RUTA PERSONALIZADA PARA BUSCAR POR TÍTULO ===============================
#     http: // localhost: 8000 / api / posts / title / Que % 20es % 20Django /
    @action(detail=False, methods=['get'], url_path='title/(?P<title>.+)')
    def retrieve_by_title(self, request, title=None):
        try:
            post = Post.objects.get(title=title)
            serializer = self.get_serializer(post)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        except Post.DoesNotExist:
            return Response(
                status=status.HTTP_404_NOT_FOUND,
                data={'error': 'Post no encontrado'}
            )

# =================================================================================================

    # DEFINO PARA CREAR POST CON EL METODO POST
    def create(self, request):
# ===================   USAMOS SERIALIZERS PARA CREAR POST =======================================
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
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

"""