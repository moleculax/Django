
# ESTE ARCHIVO SE CREA A PIE DESDE CERO
from rest_framework import serializers
from apps.categories.models import Category
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

