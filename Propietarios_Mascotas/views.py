from django.shortcuts import render, redirect
from .models import Propietario

# Create your views here.

def consultorio(request):
    return render(request, 'consultorio.html')

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
    
    return redirect('consultorio')
      
      