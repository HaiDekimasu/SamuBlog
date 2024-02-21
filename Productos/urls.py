from django.urls import path
from . import views

urlpatterns = [
    path('productos/', views.list_productos, name='list_productos'),
    path('productos/<int:product_id>/', views.product_detail, name='product_detail'),
    path('crear-producto/', views.create_product, name='create_product'),
    path('buscar-productos/', views.search_products, name='search_products'),
    path('carrito-de-compras/', views.cart, name='cart'),
    path('anadir-producto-al-carrito/', views.add_product_to_cart, name='add_product_to_cart'),
    path('eliminar-producto-del-carrito/', views.delete_product_from_cart, name='delete_product_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('confirmacion-de-compra/', views.confirmation_of_purchase, name='confirmation_of_purchase'),
]

