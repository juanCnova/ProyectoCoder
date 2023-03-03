from django.shortcuts import render
from django.http import HttpResponse
from appCoder.models import *


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
        
        curso = Curso(nombre = request.POST['curso'] , comision = request.POST['comision'])
        curso.save()

        return render(request,'appCoder/inicio.html')


    return render(request , 'appCoder/cursoFormulario.html')

