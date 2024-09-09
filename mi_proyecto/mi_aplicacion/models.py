from django.utils import timezone
from django.db import models

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=100)
    contenido = models.TextField(default="Sin contenido")
    autor = models.CharField(max_length=50)
    fecha_publicacion = models.DateField(default=timezone.now)

    
    def __str__(self) -> str:
        return self.titulo