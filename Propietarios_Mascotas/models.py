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
    
class EstadoReproductivo (models.Model):
    idEstadoReproductivo = models.AutoField(primary_key=True)
    Estado = models.CharField(max_length=50)

class Mascota (models.Model):
    idMascota = models.AutoField(primary_key=True)
    foto = models.ImageField(upload_to='fotosMascotas', null=True, blank=True)
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    raza = models.CharField(max_length=50)
    sexo = models.CharField(max_length=1)
    color = models.CharField(max_length=20)
    edad = models.IntegerField()
    meses = models.IntegerField()
    fechaNacimiento = models.DateField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    rh = models.CharField(max_length=3)
    personalidad = models.CharField(max_length=100)
    alimentacion = models.CharField(max_length=100)
    cantidadAlimento = models.CharField(max_length=100)
    frecuenciaAlimentacion = models.CharField(max_length=100)
    frecuenciaBano = models.CharField(max_length=100)
    antecedentesClinicos = models.CharField( max_length=100,null=True)
    propietario = models.ForeignKey(Propietario, on_delete=models.CASCADE)
    EstadoReproductivo = models.ForeignKey(EstadoReproductivo, on_delete=models.CASCADE)