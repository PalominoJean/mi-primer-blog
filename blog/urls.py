from django.conf.urls import include, url
from blog import views

urlpatterns=[
	url(r'^$', views.post_lista),
	url(r'^post/(?P<post_pk>[0-9]+)/$', views.post_detalle,name='post_detalle'),
	url(r'^post/nuevo/$', views.post_nuevo, name='post_nuevo'),
	url(r'^post/(?P<post_pk>[0-9]+)/editar/$', views.post_editar, name='post_editar'),
	url(r'^post/(?P<post_pk>[0-9]+)/eliminar/$', views.post_eliminar, name='post_eliminar'),
	url(r'^seleccionar/$', views.post_seleccionar_lista, name='seleccionar'),
	url(r'^post/(?P<post_pk>[0-9]+)/publicar/$', views.post_publicar, name='post_publicar'),
	url(r'^post/(?P<post_pk>[0-9]+)/comentar/$', views.comentario_nuevo, name='comentario_nuevo'),
	url(r'^comentario/(?P<comentario_pk>[0-9]+)/eliminar$', views.comentario_eliminar, name='comentario_eliminar'),
	url(r'^comentario/(?P<comentario_pk>[0-9]+)/aprobar$', views.comentario_aprobar, name='comentario_aprobar'),
]