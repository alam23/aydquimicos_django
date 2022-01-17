from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

class UltimosProductosList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()[0:4]
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)

class ProductoDetalles(APIView):
    def get_object(self, categoria_slug, producto_slug):
        try:
            return Producto.objects.filter(categoria__slug=categoria_slug).get(slug=producto_slug)
        except Producto.DoesNotExist:
            raise Http404

    def get(self, request, categoria_slug, producto_slug, format=None):
        producto = self.get_object(categoria_slug, producto_slug)
        serializer = ProductoSerializer(producto)
        return Response(serializer.data)

class CategoriaDetalles(APIView):
    def get_object(self, categoria_slug):
        try:
            return Categoria.objects.get(slug=categoria_slug)
        except Categoria.DoesNotExist:
            raise Http404
    
    def get(self, request, categoria_slug, format=None):
        categoria = self.get_object(categoria_slug)
        serializer = CategoriaSerializer(categoria)
        return Response(serializer.data)

@api_view(['POST'])
def busqueda(request):
    query = request.data.get('query', '')

    if query:
        productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    else:
        return Response({"productos": []})