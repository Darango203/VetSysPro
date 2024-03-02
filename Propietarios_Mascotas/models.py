from django.db import models

# Create your models here.

class Propietario (models.Model):
    documento = models.CharField(max_length=10, primary_key=True)
    nombres = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length=80)
    email = models.EmailField(max_length=50)
    telefono = models.CharField(max_length=10)
    nombreEmer= models.CharField(max_length=50)
    telefonoEmer = models.CharField(max_length=10)
