from django.shortcuts import render

# Create your views here.

def consultorio(request):
    return render(request, 'consultorio.html')