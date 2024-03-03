from django.urls import path
from . import views


urlpatterns = [
    path('consultorio/', views.listar_propietarios, name='listar_propietarios'),
    path('registrar_propietario/', views.registrar_propietario),
    path('Perfil_propietario/<int:documento>/', views.Perfil_Propietario),
    path('registrar_mascota/', views.Registrar_Mascota),
]

