from django.urls import path

from . import views

urlpatterns = [
    path('products/', views.list_productos, name='list_productos'),
    path('products/<int:product_id>/', views.product_detail, name='product_detail'),
    path('create_product/', views.create_product, name='create_product'),
]
