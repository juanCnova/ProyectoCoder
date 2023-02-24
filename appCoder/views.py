from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from appCoder.models import *

def info(request):
    curso1 = Curso(nombre='python',comision=1234)
    almuno1 = Estudiante(nombre='juan cruz',apellido='Novakovich',mail='juancruz.nova123@gmail.com')
    curso1.save()
    almuno1.save()

    dic = {'curso':curso1.nombre , 'comision': curso1.comision , 'estudiante':almuno1.nombre , 'mail':almuno1.mail,'apellido':almuno1.apellido}

    plantilla = loader.get_template('plantilla1.html').render(dic)

    return HttpResponse(plantilla)

def curso(request):
    curso1 = Curso(nombre='python',comision=1234)
    almuno1 = Estudiante(nombre='juan cruz',apellido='Novakovich',mail='juancruz.nova123@gmail.com')
    curso1.save()
    almuno1.save()
   
    dic = {'curso':curso1.nombre , 'comision': curso1.comision , 'estudiante':almuno1.nombre , 'mail':almuno1.mail,'apellido':almuno1.apellido}

    plantilla = loader.get_template('plantilla2.html').render(dic)

    return HttpResponse(plantilla)
