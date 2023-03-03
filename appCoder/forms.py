from django import forms

class formularioCurso(forms.Form):
    curso = forms.CharField()
    comision = forms.IntegerField()


class formularioProfesor(forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    mail = forms.EmailField()
    profesion = forms.CharField(max_length=20)

class formularioEntegable(forms.Form):
    nombre = forms.CharField(max_length=20)
    fecha = forms.IntegerField()
    entregado = forms.BooleanField()

