from django.db import models

# Create your models here.
class Cliente(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(null=True)


class Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    

class Vendedor(models.Model):

    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)


