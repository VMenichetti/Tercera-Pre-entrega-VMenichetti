from django.db import models

# Create your models here.
class Cliente (models.Model):
    usuario=models.CharField(max_length=20)
    edad=models.IntegerField()
    email=models.EmailField()
    direccion=models.CharField(max_length=40)

class Producto (models.Model):
    nombre=models.CharField(max_length=40)
    descripcion=models.CharField(max_length=80)
    precio=models.DecimalField(max_digits=4, decimal_places=2)       

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
