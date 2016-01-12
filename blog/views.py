from django.shortcuts import render
from django.utils import timezone
from blog.models import Post

# Create your views here.
def post_lista(request):
	posts=Post.objects.filter(publicacion_fecha__lte=timezone.now()).order_by('publicacion_fecha')
	return render(request,'blog/post_lista.html',{'posts':posts})