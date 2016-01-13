from django.conf.urls import include, url
from blog import views

urlpatterns=[
	url(r'^$', views.post_lista),
	url(r'^post/(?P<post_pk>[0-9]+)/$', views.post_detalle),
	url(r'^post/nuevo/$', views.post_nuevo, name='post_nuevo'),
	url(r'^post/(?P<post_pk>[0-9]+)/editar/$', views.post_editar, name='post_editar'),
	url(r'^post/(?P<post_pk>[0-9]+)/eliminar/$', views.post_eliminar, name='post_eliminar'),
]