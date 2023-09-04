from django.db import models

# Create your models here.
class Athlete(models.Model):
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.nombre} {self.apellido}'
    
    class Meta():
        ordering = ('nombre', 'apellido')


class Competitions(models.Model):
    
    nombre = models.CharField(max_length=50)
    arena = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
    
    class Meta():
        verbose_name = 'Competition'
        verbose_name_plural = 'Competitions'
    

class Store(models.Model):

    producto = models.CharField(max_length=50)
    precio = models.IntegerField()

    def __str__(self):
        return self.producto
    
    class Meta():
        verbose_name = 'Store'
        verbose_name_plural = 'Store'