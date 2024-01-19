from django.urls import path

from . import views

urlpatterns = [
    path('productos/', views.list_productos, name='list_productos'),
    path('productos/<int:product_id>/', views.product_detail, name='product_detail'),
    path('crear-producto/', views.create_product, name='create_product'),
]
