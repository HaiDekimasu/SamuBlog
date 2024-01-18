from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect

from .models import Productos, Category

def list_productos(request):
    productos = Productos.objects.all()
    return render(request, 'productos.html', {'productos': productos})

def product_detail(request, product_id):
    product = get_object_or_404(Productos, pk=product_id)
    return render(request, 'product_detail.html', {'product': product})

def create_product(request):
    if request.method == 'POST':
        name = request.POST['name']
        price = request.POST['price']
        descripcion = request.POST['descripcion']
        category_id = request.POST['category']

        category = Category.objects.get(id=category_id)

        product = Productos(name=name, price=price, descripcion=descripcion, category=category)
        product.save()

        return HttpResponseRedirect('/products')
    else:
        categories = Category.objects.all()
        return render(request, 'create_product.html', {'categories': categories})
