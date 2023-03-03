from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=20)
    comision = models.IntegerField()

class Estudiante(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()

class Profesor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()
    profesion = models.CharField(max_length=20)

class Entegable(models.Model):
    nombre = models.CharField(max_length=20)
    fecha = models.IntegerField()
    entregado = models.BooleanField()

class Tutor(models.Model):
    nombre = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    mail = models.EmailField()
    Profesion = models.CharField(max_length=20)
