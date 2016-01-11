from django.db import models
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

# Create your models here.


class Categoria(models.Model):
	Nombre = models.CharField(max_length = 100) 
	
	def __unicode__(self):
		return self.Nombre
		
		
class Noticia(models.Model):
	Estados = (
		('0', 'Desactivado'),
		('1', 'Activado'),
	)
	Titulo = models.CharField(max_length = 200)
	SubTitulo = models.CharField(max_length = 500, null = True,blank = True)
	Contenido = models.TextField()
	Etiquetas = models.CharField(max_length = 100, null = True,blank = True)
	Imagen = models.ImageField(upload_to='img', null=True,blank = True)
	Fecha = models.DateTimeField(auto_now_add=True)
	Categoria = models.ManyToManyField(Categoria,blank = True)
	Estado = models.CharField(max_length=1,choices=Estados)
	Autor = models.ForeignKey(User)
	
	def __unicode__(self):
		return self.Titulo
	

class Comentarios(models.Model):
	Estados = (
		('0', 'Desactivado'),
		('1', 'Activado'),
	)
	Comentario = models.TextField()
	Estado = models.CharField(max_length=1,choices=Estados)
	Nombre = models.CharField(max_length = 200, null = True,blank = True)
	Email = models.EmailField(max_length = 254)
	Fecha = models.DateTimeField(auto_now_add=True)
	Apellidos = models.CharField(max_length = 200, null = True,blank = True)
	Noticia = models.ForeignKey(Noticia)
	class Meta:
		unique_together = (("Email", "Fecha"),)
	
	def __unicode__(self):
		return self.Comentario
	

