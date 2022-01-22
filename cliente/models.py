from django.db import models
from django.contrib.auth.models import User

TIPO_CLIENTES = (
    ('normal','Normal'),
    ('empresa','Empresa'),
)

class Cliente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_cliente = models.CharField(max_length=30, choices=TIPO_CLIENTES, default='normal')
    telefono = models.IntegerField(blank=True)
    direccion = models.CharField(max_length=100, blank=True)
    
    def __str__(self):
        return self.user.username