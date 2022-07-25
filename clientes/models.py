from django.db import models

# Create your models here.

class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=40)
    documento=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return f'Nombre: {self.nombre} - Apellido: {self.apellido} - Documento: {self.documento} Email: {self.email} '