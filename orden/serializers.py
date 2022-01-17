from rest_framework import serializers

from .models import Orden, OrdenItem

from producto.serializers import ProductoSerializer

class MyOrdenItemSerializer(serializers.ModelSerializer):    
    producto = ProductoSerializer()

    class Meta:
        model = OrdenItem
        fields = (
            "precio",
            "producto",
            "cantidad",
        )

class MyOrdenSerializer(serializers.ModelSerializer):
    items = MyOrdenItemSerializer(many=True)

    class Meta:
        model = Orden
        fields = (
            "id",
            "nombre",
            "apellido",
            "email",
            "direccion",
            "codigo_zip",
            "lugar",
            "celular",
            "stripe_token",
            "items",
            "monto_pagado"
        )

class OrdenItemSerializer(serializers.ModelSerializer):    
    class Meta:
        model = OrdenItem
        fields = (
            "precio",
            "producto",
            "cantidad",
        )

class OrdenSerializer(serializers.ModelSerializer):
    items = OrdenItemSerializer(many=True)

    class Meta:
        model = Orden
        fields = (
            "id",
            "nombre",
            "apellido",
            "email",
            "direccion",
            "codigo_zip",
            "lugar",
            "celular",
            "stripe_token",
            "items",
        )
    
    def create(self, validated_data):
        items_data = validated_data.pop('items')
        orden = Orden.objects.create(**validated_data)

        for item_data in items_data:
            OrdenItem.objects.create(orden=orden, **item_data)
            
        return orden