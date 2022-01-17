from django.contrib.auth.models import User
from django.db import models

from producto.models import Producto

class Orden(models.Model):
    usuario = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)
    codigo_zip = models.CharField(max_length=100)
    lugar = models.CharField(max_length=100)
    celular = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    monto_pagado = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    stripe_token = models.CharField(max_length=100)

    class Meta:
        ordering = ['-created_at',]
    
    def __str__(self):
        return self.nombre

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, related_name='items', on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, related_name='items', on_delete=models.CASCADE)
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    cantidad = models.IntegerField(default=1)

    def __str__(self):
        return '%s' % self.id