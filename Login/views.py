from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('usuario')
        password = request.POST.get('clave')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            # Redireccionar al usuario a la página de consultorio en caso de que el usuario este registrado
            return redirect('listar_propietarios')
        else:
            # Manejar caso de credenciales inválidas en caso de que el usuario no este registrado
            return render(request, 'login.html', {'error_message': 'Credenciales inválidas'})
    else:
        return render(request, 'login.html')
