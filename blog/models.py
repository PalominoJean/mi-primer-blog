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