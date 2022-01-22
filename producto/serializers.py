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
            "get_thumbnail"
        )
class CategoriaSerializer(serializers.ModelSerializer):
    productos = ProductoSerializer(many=True)

    class Meta:
        model = Categoria
        fields = [
            "id",
            "nombre",
            "get_absolute_url",
            "productos",
            "slug"
        ]