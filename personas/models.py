from django.db import models


class Cliente(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    dni = models.IntegerField()

    def __str__(self):
        return f"{self.nombre}, {self.apellido}"
