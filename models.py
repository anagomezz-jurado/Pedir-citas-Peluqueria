
from django.db import models



class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    telefono = models.FloatField()

    def __str__(self):
        return(self.nombre)

class Dependienta(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return(self.nombre)

class Cita(models.Model):
    nombre = models.ManyToManyField(Cliente)
    fecha = models.DateTimeField()
    hora = models.TimeField(auto_now=False)
    servicio = models.CharField(max_length=100)
    dependienta = models.ForeignKey(Dependienta, on_delete=models.CASCADE, default="")




