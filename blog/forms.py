from django.forms import ModelForm
from django import forms
from blog.models import Noticia, Categoria, Comentarios

class NoticiaForm(forms.ModelForm):
	class Meta:
		model = Noticia
			
		fields = ['Titulo','SubTitulo','Contenido','Etiquetas','Imagen','Categoria','Estado']
	
	def __init__(self, *args, **kwargs):
		super(NoticiaForm, self).__init__(*args,**kwargs)
 		self.fields['Titulo'].widget.attrs['class'] = 'form-control'
		self.fields['SubTitulo'].widget.attrs['class'] = 'form-control'
		self.fields['Contenido'].widget.attrs['class'] = 'form-control'
		self.fields['Etiquetas'].widget.attrs['class'] = 'form-control'
		self.fields['Imagen'].widget.attrs['class'] = 'form-control'
		self.fields['Categoria'].widget.attrs['class'] = 'form-control'
		self.fields['Estado'].widget.attrs['class'] = 'form-control'
		
class searchForm(ModelForm):
	class Meta:
		fields = ['q']

class CategoriaForm(ModelForm):
	class Meta:
		model = Categoria
		
		fields = ['Nombre']
	
	def __init__(self, *args, **kwargs):
		super(CategoriaForm, self).__init__(*args, **kwargs)
		self.fields['Nombre'].label = "Categoria "

class ComentarioForm(ModelForm):
	class Meta:
		model = Comentarios
		fields = ['Nombre','Apellidos','Email','Comentario']

