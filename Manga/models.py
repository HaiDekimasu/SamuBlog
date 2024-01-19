from django.db import models
# Create your models here.
class Manga(models.Model):
    
    title = models.CharField(max_length=100)
    img = models.ImageField(upload_to='img/')
    text = models.TextField(max_length=300)
    id = models.AutoField(primary_key=True)

    def __str__(self)-> str:
        return self.title

