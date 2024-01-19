from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)
    
def __str__(self):
    return self.name
    
class Productos(models.Model):
    image = models.ImageField(upload_to='product_images',default='default.jpg')
    name = models.CharField(max_length=255)
    descripcion = models.CharField(max_length=400)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)

def __str__(self):
        return self.name