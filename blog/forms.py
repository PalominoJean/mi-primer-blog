from django import forms
from blog.models import Post, Comentario

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields=('titulo','texto',)

class ComentarioForm(forms.ModelForm):
	class Meta:
		model=Comentario
		fields=('autor','texto',)