from django.db import models

# Create your models here.

class Familia(models.Model):
    nombre = models.CharField(max_length=30)
    edad = models.IntegerField()
    nacimiento = models.DateField()

    def __str__(self):
        return f'Nombre: {self.nombre} Edad: {self.edad} Nacimiento: {self.nacimiento}'