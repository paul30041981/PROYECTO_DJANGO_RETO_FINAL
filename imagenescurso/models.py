from django.db import models
from curso.models import Curso

# Create your models here.
class Imagenescurso(models.Model):
  id = models.AutoField(primary_key=True)
  curso = models.ForeignKey(Curso, related_name='imagenes',on_delete=models.CASCADE)
  url = models.CharField(max_length=255)
  gift = models.CharField(max_length=255,null=True)

  def __str__(self):
      return '{}'.format(self.curso,self.url)

  class Meta:
      verbose_name_plural = "Imagenescursos"