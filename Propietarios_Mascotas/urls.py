from django.urls import path
from . import views

urlpatterns = [
    path('consultorio/', views.consultorio, name='consultorio'),
    path('registrar_propietario/', views.registrar_propietario),
]

