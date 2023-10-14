from django.db import models

# Create your models here.

from django.db import models


# Create your models here.
class Curso(models.Model):
    idcurso= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    duracion = models.CharField(max_length=50)
    precio_individual = models.DecimalField(max_digits=10, decimal_places=2)
    precio_grupal = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='curso_imagenes/')

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    idusuario= models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=254)
    direccion = models.CharField(max_length=200)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.nombre

