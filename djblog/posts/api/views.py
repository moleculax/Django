from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import posts
# TRAEMOS EL MODELO
from posts.models import Post


class PostAPIView(APIView):
    def get(self,request):
        posts = Post.objects.all()
        data = []
        for post in posts:
            data.append({
                'id': post.id,
                'title': post.title,
                'description': post.description,
                'order': post.order,
                'status': post.status,
                'create_at': post.create_at,
                'update_at': post.update_at
            })
        return Response(status=status.HTTP_200_OK,data=data)

    # DEFINO PARA CREAR POST CON EL METODO POST
    def post(self,request):
        # OBTENGO LOS DATOS DEL BODY DE LA PETICION
        data = request.data
        # CREO UN NUEVO POST CON LOS DATOS OBTENIDOS
        post = Post.objects.create(
            title=data.get('title'),
            description=data.get('description'),
            order=data.get('order', 1),  # SI NO SE PROPORCIONA, SE ASIGNA 1 POR DEFECTO
            status=data.get('status', True)  # SI NO SE PROPORCIONA, SE ASIGNA True POR DEFECTO
        )
        # DEVUELVO UNA RESPUESTA CON EL POST CREADO Y EL CODIGO DE ESTADO 201 (CREATED)
        return Response(status=status.HTTP_201_CREATED, data={
            'title': post.title,
            'description': post.description,
            'order': post.order,
        })

