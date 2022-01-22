from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User

from rest_framework import status, authentication, permissions
from .serializers import ClienteSerializer
from .models import Cliente
from rest_framework.response import Response

class ClienteDetalles(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):
        cliente = Cliente.objects.get(user=request.user)
        serializer = ClienteSerializer(cliente)
        return Response(serializer.data)