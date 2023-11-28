from django import forms
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.db.models import ProtectedError

from . import models

class MetaForm(forms.ModelForm):
    class Meta:
        model=models.MetaModelo
        fields=['descripcion']
    
class TemaForm(forms.ModelForm):
    class Meta:
        model = models.Tema
        fields=['nombre'] 
      
class EventoForm(forms.ModelForm):
    class Meta:
        model = models.Evento
        fields=['conferencia','cursos','tema','escuela','fecha','apoyo',
                'cant_hombres','cant_mujeres','dirigido']

class FechaForm(forms.ModelForm):
    class Meta:
        model = models.getFecha
        fields=['fecha_inicio','fecha_fin']