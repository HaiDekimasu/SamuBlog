from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Productos, Category


def list_productos(request):
    categoria_id = request.GET.get('categoria', None)  # Obtener el filtro de categoría de la URL
    if categoria_id:
        productos = Productos.objects.filter(category_id=categoria_id)  # Filtrar productos por categoría
        if not productos.exists():
            return render(request, 'productos.html', {'productos': [], 'error': 'No hay productos en esta categoría'})
    else:
        productos = Productos.objects.all()  # Mostrar todos los productos si no hay filtro
    return render(request, 'productos.html', {'productos': productos})


def product_detail(request, product_id):
    product = get_object_or_404(Productos, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        # ... (código de creación de producto)
        return HttpResponseRedirect(reverse('list_productos'))  # Redirección a la lista de productos
    else:
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories': categories})
