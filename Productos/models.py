from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Producto, Categoria, UsuarioCarrito, Carrito, CarritoItem, Orden, OrdenItem
class Categoria(models.Model):
    nombre = models.CharField(max_length=255)

class Producto(models.Model):
    nombre = models.CharField(max_length=255)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='productos/')

class UsuarioCarrito(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    sesion = models.CharField(max_length=255, unique=True)

class Carrito(models.Model):
    usuario_carrito = models.OneToOneField(UsuarioCarrito, on_delete=models.CASCADE)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    estado = models.CharField(max_length=255, choices=[('abierto', 'Abierto'), ('cerrado', 'Cerrado')], default='abierto')
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    impuesto_total = models.DecimalField(max_digits=10, decimal_places=2, default=0.0)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    direccion_envio = models.TextField(null=True, blank=True)
    metodo_pago = models.CharField(max_length=255, choices=[('efectivo', 'Efectivo'), ('tarjeta', 'Tarjeta de crédito/débito')], null=True, blank=True)
    productos = models.ManyToManyField(Producto, through=CarritoItem)

class CarritoItem(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    sesion = models.CharField(max_length=255, null=True, blank=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha_compra = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    # Puedes añadir más campos para información de facturación, envío, etc.

class OrdenItem(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField()
    # Puedes añadir campos adicionales para guardar el precio unitario, etc.
