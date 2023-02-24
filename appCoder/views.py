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

    

