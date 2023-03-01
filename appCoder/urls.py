from django.urls import path
from appCoder.views import *


urlpatterns = [
    path('',inicio, name='Inicio'),
    path('curso/',curso, name='Cursos'),
    path('profesores/',profesores, name='Profesores'),
    path('estudiantes/',estudiantes, name='Estudiantes'),
    path('entregables/',entregables, name='Entregables'),
    
]