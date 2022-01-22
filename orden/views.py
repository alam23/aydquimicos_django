import stripe

from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import (
    api_view,
    authentication_classes,
    permission_classes,
)
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Orden, OrdenItem
from .serializers import OrdenSerializer, MyOrdenSerializer


@api_view(["POST"])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrdenSerializer(data=request.data)
    if serializer.is_valid():
        stripe.api_key = settings.STRIPE_SECRET_KEY
        paid_amount = sum(
            item.get("cantidad") * item.get("producto").precio
            for item in serializer.validated_data["items"]
        )

        try:
            charge = stripe.Charge.create(
                amount=int(paid_amount * 100),
                currency="USD",
                description="Cobro de A&DQuimicos",
                source=serializer.validated_data["stripe_token"],
            )
            print("charge funciona")
            serializer.save(usuario=request.user, monto_pagado=paid_amount)
            print("serializer funciona")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Orden.objects.filter(usuario=request.user)
        serializer = MyOrdenSerializer(orders, many=True)
        return Response(serializer.data)
