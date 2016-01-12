from django.shortcuts import render,get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def post_lista(request):
	posts=Post.objects.filter(publicacion_fecha__lte=timezone.now()).order_by('publicacion_fecha')
	return render(request,'blog/post_lista.html',{'posts':posts})

def post_detalle(request,post_pk):
	post=get_object_or_404(Post,pk=post_pk)
	return render(request, 'blog/post_detalle.html',{'post':post})