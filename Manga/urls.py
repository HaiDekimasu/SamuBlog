from django.urls import path
from . import views

urlpatterns = [
    path('manga/', views.manga, name='manga'),
    path('download-pdf/', views.Tomo1, name='download-pdf'),
    path('download2-pdf/', views.Tomo2, name='download2-pdf'),
    path('download3-pdf/', views.Tomo3, name='download3-pdf')
]
