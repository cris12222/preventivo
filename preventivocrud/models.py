from django.db import models
from safedelete.models import SOFT_DELETE_CASCADE, SafeDeleteModel


class MetaModelo( SafeDeleteModel, models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    descripcion = models.CharField(max_length=255)
    class Meta:
        db_table = 'metas'
        ordering = ['-id']

class Tema( SafeDeleteModel,models.Model):
    _safedelete_policy = SOFT_DELETE_CASCADE
    nombre = models.CharField(max_length=255)
    class Meta:
        db_table = 'temas'
        ordering = ['id']
    def __str__(self):
        return self.nombre
  
class Evento( SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    conferencia= models.IntegerField()
    cursos = models.IntegerField()
    tema = models.ForeignKey('Tema',on_delete=models.DO_NOTHING,null=True)
    escuela = models.CharField(max_length=255)
    fecha = models.DateTimeField()
    apoyo = models.CharField(max_length=255)
    cant_hombres = models.IntegerField()
    cant_mujeres = models.IntegerField()
    dirigido=models.CharField(max_length=255)
    class Meta:
        db_table = 'eventos'
        ordering = ['-id']
    
class getFecha(models.Model):
    fecha_inicio = models.DateTimeField()
    fecha_fin = models.DateTimeField()
    def __str__(self):
        return f"{self.fecha_inicio}/{self.fecha_fin}"
    