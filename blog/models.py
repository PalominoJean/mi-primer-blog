from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
	autor=models.ForeignKey('auth.User')
	titulo=models.CharField(max_length=200)
	texto=models.TextField()
	creacion_fecha=models.DateTimeField(default=timezone.now)
	publicacion_fecha=models.DateTimeField(blank=True,null=True)
	def publicar(self):
		self.publicacion_fecha=timezone.now()
		self.save()
	def __str__(self):
		return self.titulo
	def comentarios_aprobados(self):
		return self.comentarios.filter(aprobado=True)

class Comentario(models.Model):
	post=models.ForeignKey('Post',related_name="comentarios")
	autor=models.CharField(max_length=30)
	texto=models.TextField()
	creacion_fecha=models.DateTimeField(default=timezone.now)
	aprobado=models.BooleanField(default=False)
	def aprobar(self):
		self.aprobado=True
		self.save()
	def __str__(self):
		return self.texto
