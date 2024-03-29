# Generated by Django 4.0.1 on 2022-01-15 20:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('producto', '0002_producto'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orden',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('direccion', models.CharField(max_length=100)),
                ('codigo_zip', models.CharField(max_length=100)),
                ('lugar', models.CharField(max_length=100)),
                ('celular', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('monto_pagado', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('stripe_token', models.CharField(max_length=100)),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='OrdenItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('precio', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cantidad', models.IntegerField(default=1)),
                ('orden', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='orden.orden')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='items', to='producto.producto')),
            ],
        ),
    ]
