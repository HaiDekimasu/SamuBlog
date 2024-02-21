from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Productos, Category

def list_productos(request):
    categoria_id = request.GET.get('categoria', None)
    if categoria_id:
        productos = Productos.objects.filter(category_id=categoria_id)
        if not productos.exists():
            return render(request, 'productos.html', {'productos': [], 'error': 'No hay productos en esta categoría'})
    else:
        productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})


def product_detail(request, product_id):
    product = get_object_or_404(Productos, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})


def create_product(request):
    if request.method == 'POST':
        # ... (código de creación de producto)
        return HttpResponseRedirect(reverse('list_productos'))
    else:
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories': categories})


def search_products(request):
    query = request.GET.get('q', None)
    if query:
        productos = Productos.objects.filter(name__icontains=query)
        return render(request, 'search_products.html', {'productos': productos})
    else:
        return render(request, 'search_products.html', {'error': 'No se encontraron productos'})


def cart(request):
    productos_en_carrito = request.session.get('productos_en_carrito', {})
    productos = []
    for producto_id, cantidad in productos_en_carrito.items():
        producto = Productos.objects.get(pk=producto_id)
        producto.cantidad = cantidad
        productos.append(producto)
    total = sum(producto.price * producto.cantidad for producto in productos)
    return render(request, 'cart.html', {'productos': productos, 'total': total})


def add_product_to_cart(request):
    producto_id = request.POST.get('producto_id')
    cantidad = request.POST.get('cantidad')
    productos_en_carrito = request.session.get('productos_en_carrito', {})
    productos_en_carrito[producto_id] = cantidad
    request.session['productos_en_carrito'] = productos_en_carrito
    return HttpResponseRedirect(reverse('cart'))


def delete_product_from_cart(request):
    producto_id = request.POST.get('producto_id')
    productos_en_carrito = request.session.get('productos_en_carrito', {})
    del productos_en_carrito[producto_id]
    request.session['productos_en_carrito'] = productos_en_carrito
    return HttpResponseRedirect(reverse('cart'))


def checkout(request):
    if request.method == 'POST':
        # ... (código de procesamiento de pago)
        return HttpResponseRedirect(reverse('confirmation_of_purchase'))
    else:
        productos_en_carrito = request.session.get('productos_en_carrito', {})
        productos = []
        for producto_id, cantidad in productos_en_carrito.items():
            producto = Productos.objects.get(pk=producto_id)
            producto.cantidad = cantidad
            productos.append(producto)
        total = sum(producto.price * producto.cantidad for producto in productos)
        return render(request, 'checkout.html', {'productos': productos, 'total': total})


def confirmation_of_purchase(request):
    # Obtener información del usuario y la compra
    usuario = request.user
    productos_en_carrito = request.session.get('productos_en_carrito', {})
    productos = []
    for producto_id, cantidad in productos_en_carrito.items():
        producto = Productos.objects.get(pk=producto_id)
        producto.cantidad = cantidad
        productos.append(producto)
    total = sum(producto.price * producto.cantidad for producto in productos)
    
    # Guardar la información de la compra en la base de datos
    # ... (código para guardar la compra)
    
    # Eliminar los productos del carrito
    request.session['productos_en_carrito'] = {}
    
    return render(request, 'confirmation_of_purchase.html', {'usuario': usuario, 'productos': productos, 'total': total})