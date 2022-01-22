from rest_framework import serializers
from django.contrib.auth.models import User
from djoser.serializers import UserSerializer
from .models import Cliente

# class ClienteSerializer(UserSerializer):
#     class Meta(UserSerializer.Meta):
#          fields = ('id', 
#                     'email', 
#                     'first_name',
#                     'last_name',
#                 )

class ClienteSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=True)
    class Meta:
        model = Cliente
        fields = ('user','tipo_cliente', 'telefono', 'direccion',)
