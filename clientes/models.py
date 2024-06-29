# clientes/models.py

from django.db import models

class Genero(models.Model):
    id_genero = models.AutoField(primary_key=True)
    nombre_genero = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_genero

class Cliente(models.Model):
    rut = models.CharField(max_length=12, unique=True)
    nombre = models.CharField(max_length=100)
    apellido_paterno = models.CharField(max_length=100)
    apellido_materno = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20)
    email = models.EmailField()
    direccion = models.CharField(max_length=200)
    activo = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre


