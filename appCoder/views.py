from django.shortcuts import render
from django.http import HttpResponse
from appCoder.models import *
from appCoder.forms import *


def inicio(request):
    return render(request,'appCoder/inicio.html')


def curso(request):
    return render(request,'appCoder/curso.html')


def profesores(request):
    return render(request,'appCoder/profesores.html')
    

def estudiantes(request):
    return render(request,'appCoder/estudiantes.html')
    

def entregables(request):
    return render(request,'appCoder/entregables.html')

    
def cursoFormulario(request):
 
    if request.method == 'POST':
        
        formulario = formularioCurso(request.POST)
        

        if formulario.is_valid():
            info = formulario.cleaned_data

            curso = Curso(nombre=info['curso'] , comision=info['comision'])
            curso.save()

        return render(request,'appCoder/inicio.html')

    else:
        formulario = formularioCurso()

    return render(request , 'appCoder/cursoFormulario.html',{'formulario':formulario})


def profesorFormulario(request):

    if request.method == 'POST':
        
        formulario = formularioProfesor(request.POST)
        

        if formulario.is_valid():
            info = formulario.cleaned_data

            profe = Profesor(nombre=info['nombre'] , apellido=info['apellido'], mail=info['mail'] , profesion=info['profesion'])
            profe.save()

        return render(request,'appCoder/inicio.html')

    else:
        formulario = formularioProfesor()

    return render(request , 'appCoder/profeFormulario.html',{'formulario':formulario})


def entregableFormulario(request):

    if request.method == 'POST':
        
        formulario = formularioEntegable(request.POST)
        

        if formulario.is_valid():
            info = formulario.cleaned_data

            entre = Entegable(nombre=info['nombre'] , fecha=info['fecha'], entregado=info['entregado'] )
            entre.save()

        return render(request,'appCoder/inicio.html')

    else:
        formulario = formularioEntegable()

    return render(request , 'appCoder/entregableFormulario.html',{'formulario':formulario})
