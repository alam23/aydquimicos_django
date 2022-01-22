from rest_framework import serializers

from .models import Producto, Categoria

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = (
            "id",
            "nombre",
            "get_absolute_url",
            "descripcion",
            "precio",
            "get_image",
            "get_thumbnail",
            "es_arriesgado"
        )
        
    # def to_representation(self, instance):
    #     response = super().to_representation(instance)
    #     print(response)
    #     response['categoria'] = CategoriaSerializer(instance.categoria).data
    #     return response

class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True, read_only=True)

    class Meta:
        model = Categoria
        fields = [
            "id",
            "nombre",
            "get_absolute_url",
            "productos",
            "slug"
        ]