from django.db import models

# Create your models here.
class Capitulos(models.Model):
    title = models.CharField(max_length=100)
    iframe_url = models.CharField(max_length=255, blank=True)
    text = models.TextField(max_length=1000)
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title   