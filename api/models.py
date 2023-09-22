from django.db import models

# Create your models here.
class apuntes (models.Model):
    titulo = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=100)
    fecha = models.DateField( auto_now=True)
    archivo = models.FileField(upload_to="apuntes")
    def __str__(self):
        return self.titulo