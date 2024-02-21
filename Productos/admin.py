from django.contrib import admin
from .models import Producto, Categoria, UsuarioCarrito, Carrito, CarritoItem, Orden, OrdenItem

# Register your models here.
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(UsuarioCarrito)
admin.site.register(Carrito)
admin.site.register(CarritoItem)
admin.site.register(Orden)
admin.site.register(OrdenItem)

