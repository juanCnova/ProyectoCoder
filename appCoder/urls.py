from django.urls import path
from appCoder.views import *


urlpatterns = [
    path('',inicio),
    path('curso/',curso),
    path('profesores/',profesores),
    path('estudiantes/',estudiantes),
    path('entregables/',entregables),
    
]