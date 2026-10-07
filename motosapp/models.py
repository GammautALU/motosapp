from django.db import models

class Moto(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    anio = models.IntegerField()
    cilindrada = models.IntegerField()
    precio = models.IntegerField()
