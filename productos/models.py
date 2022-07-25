from django.db import models

# Create your models here.

class CategoriaProd(models.Model):
    nombre=models.CharField(max_length=50)


    def __str__(self):
        return f'{self.nombre}'

class Productos(models.Model):
    imagen=models.ImageField()
    categoria=models.ForeignKey(CategoriaProd, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=40)
    precio=models.FloatField()


    def __str__(self):
        return f'Categoria:{self.categoria} Nombre: {self.nombre} - Precio: {self.precio}'
          



