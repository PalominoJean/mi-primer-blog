from django.shortcuts import render,get_object_or_404, redirect
from django.utils import timezone
from blog.models import Post
from blog.forms import PostForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def post_lista(request):
	posts=Post.objects.filter(publicacion_fecha__lte=timezone.now()).order_by('publicacion_fecha')
	return render(request,'blog/post_lista.html',{'posts':posts})

def post_detalle(request,post_pk):
	post=get_object_or_404(Post,pk=post_pk)
	return render(request, 'blog/post_detalle.html',{'post':post})

@login_required
def post_nuevo(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.publicacion_fecha = timezone.now()
			post.save()
			return redirect('blog.views.post_detalle', post_pk=post.pk)
	else:
		form = PostForm()
	return render(request, 'blog/post_nuevo.html', {'form': form})	

@login_required
def post_editar(request,post_pk):
	post=get_object_or_404(Post,pk=post_pk)
	if request.method=="POST":
		form=PostForm(request.POST, instance=post)
		if form.is_valid():
			post=form.save(commit=False)
			post.autor = request.user
			post.save()
			return redirect('blog.views.post_detalle',post_pk=post.pk)
	else:
		form=PostForm(instance=post)
	return render(request,'blog/post_nuevo.html',{'form':form})

@login_required
def post_eliminar(request,post_pk):
	post=get_object_or_404(Post,pk=post_pk)
	post.delete()
	return redirect('blog.views.post_lista')

@login_required
def post_seleccionar_lista(request):
	posts=Post.objects.filter(publicacion_fecha__isnull=True).order_by('creacion_fecha')
	return render(request,'blog/post_seleccionar_lista.html',{'posts':posts}) 

@login_required
def post_publicar(request,post_pk):
	post=get_object_or_404(Post,pk=post_pk)
	post.publicar()
	return redirect('blog.views.post_detalle',post_pk=post.pk)