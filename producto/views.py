from django.db.models import Q
from django.http import Http404, HttpResponse, JsonResponse

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Producto, Categoria
from .serializers import ProductoSerializer, CategoriaSerializer

from rest_framework.parsers import JSONParser


class UltimosProductosList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()[0:4]
        print(productos)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class AllProductsList(APIView):
    def get(self, request, format=None):
        productos = Producto.objects.all()
        print(productos)
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)


class CategoriaList(APIView):
    def get(self, request, format=None):
        categorias = Categoria.objects.all()
        print("Categorias", categorias)
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)


class ProductoDetalles(APIView):
    def get_object(self, categoria_slug, producto_slug):
        try:
            return Producto.objects.filter(categoria__slug=categoria_slug).get(
                slug=producto_slug
            )
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


@api_view(["POST"])
def busqueda(request):
    # * Query es el cuerpo que se mandara para buscar
    query = request.data.get("query", "")

    if query:
        productos = Producto.objects.filter(
            Q(nombre__icontains=query) | Q(descripcion__icontains=query)
        )
        serializer = ProductoSerializer(productos, many=True)
        return Response(serializer.data)
    else:
        return Response({"productos": []})


@api_view(["POST"])
def createProduct(request):
    # * Query es el cuerpo que se mandara para buscar
    body = JSONParser().parse(request)
    serializer = ProductoSerializer(data=body)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)


@api_view(["POST"])
def createCategory(request):
    # * Query es el cuerpo que se mandara para buscar
    body = JSONParser().parse(request)
    serializer = CategoriaSerializer(data=body)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)

    # if query:
    #     productos = Producto.objects.filter(Q(nombre__icontains=query) | Q(descripcion__icontains=query))
    #     serializer = ProductoSerializer(productos, many=True)
    #     return Response(serializer.data)
    # else:
    #     return Response({"productos": []})

@api_view(["PUT"])
def updateCategory(request,pk):
    categoria = Categoria.objects.get(id=pk)
    serializer = CategoriaSerializer(instance=categoria, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    return JsonResponse(serializer.errors, status=400)

@api_view(["DELETE"])
def deleteCategory(request, pk):
    # * Query es el cuerpo que se mandara para buscar
    category = Categoria.objects.get(id=pk)
    category.delete()

    return Response({"message": "Categoria eliminada correctamente"})
