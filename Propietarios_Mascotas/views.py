from django.shortcuts import render, redirect
from .models import Propietario, Mascota, EstadoReproductivo
# Create your views here.


def registrar_propietario(request):
    documento = request.POST.get('txtDocumentoP')
    nombres = request.POST.get('txtNombreP')
    apellidos = request.POST.get('txtApellidosP')
    direccion = request.POST.get('txtDireccionP')
    email = request.POST.get('txtEmailP')
    telefono = request.POST.get('txtTelP')
    nombreEmer = request.POST.get('txtNombreE')
    telefonoEmer = request.POST.get('txtTelE')
    
    propietario = Propietario.objects.create(documento=documento, nombres=nombres, apellidos=apellidos, direccion=direccion, email=email, telefono=telefono, nombreEmer=nombreEmer, telefonoEmer=telefonoEmer)
    propietario = Propietario.objects.get(documento=documento)
    
    
    return render(request, 'Perfil_propietario.html', {'propietario':propietario} )

def listar_propietarios(request):
    propietarios = Propietario.objects.all()
    return render(request, 'consultorio.html', {'propietarios':propietarios})

def Perfil_Propietario(request, documento):
    estados = EstadoReproductivo.objects.all()
    propietarios = Propietario.objects.all()
    propietario = Propietario.objects.get(documento=documento)
    mascotas = Mascota.objects.filter(propietario=propietario)
    return render(request, 'Perfil_propietario.html', {'propietario': propietario, 'estados': estados, 'propietarios': propietarios, 'mascotas': mascotas})

def Registrar_Mascota(request):
    
    propietarios = Propietario.objects.all()
    estados = EstadoReproductivo.objects.all()
    
    idMascota = request.POST.get('txtIdMascota')
    foto = request.POST.get('txtFoto')
    nombre = request.POST.get('txtNombreMascota')
    especie = request.POST.get('txtEspecie')
    raza = request.POST.get('txtRaza')
    sexo = request.POST.get('txtSexo')
    color = request.POST.get('txtColor')
    edad = request.POST.get('txtEdad')
    meses = request.POST.get('txtMeses')
    fechaNacimiento = request.POST.get('txtFechaNacimiento')
    peso = request.POST.get('txtPeso')
    rh = request.POST.get('txtRH')
    personalidad = request.POST.get('txtPersonalidad')
    alimentacion = request.POST.get('txtAlimentacion')
    cantidadAlimento = request.POST.get('txtCantidadAlimento')
    frecuenciaAlimentacion = request.POST.get('txtFrecuenciaAlimentacion')
    frecuenciaBano = request.POST.get('txtFrecuenciaBano')
    antecedentesClinicos = request.POST.get('txtAntecedentesClinicos')
    propietario = request.POST.get('txtPropietario')
    Estados = request.POST.get('txtEstadoReproductivo')
    
    propietario = Propietario.objects.get(pk=propietario)
    estados = EstadoReproductivo.objects.get(pk=Estados)

   
    mascota = Mascota.objects.create(idMascota=idMascota, foto=foto, nombre=nombre, especie=especie, raza=raza, sexo=sexo, color=color, edad=edad, meses=meses, fechaNacimiento=fechaNacimiento, peso=peso, rh=rh, personalidad=personalidad, alimentacion=alimentacion, cantidadAlimento=cantidadAlimento, frecuenciaAlimentacion=frecuenciaAlimentacion, frecuenciaBano=frecuenciaBano, antecedentesClinicos=antecedentesClinicos, propietario=propietario, EstadoReproductivo=estados)
    return render(request, 'consultorio.html', {'propietario':propietario , 'estados': estados} )

def listar_mascotas(request):
    mascotas = Mascota.objects.all()
    return render(request, 'consultorio.html', {'mascotas':mascotas})