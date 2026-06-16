from rest_framework.serializers import ModelSerializer
from posts.models import Post
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        # SOLO TARIGO LOS QUE QUIERO
        fields = ('title', 'description', 'order', 'status', 'create_at', 'update_at')
       # TRAERIA TODO PERO NO ES RECOMENDABLE
       # fields = '__all__'


    # PODEMOS CREAR OTRAS CLASS CON SERIALIZADORES CON LOS DATOS DE POST QUE NECESITEMOS