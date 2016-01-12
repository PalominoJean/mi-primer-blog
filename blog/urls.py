from django.conf.urls import url
from blog import views

urlpatterns=[
	url(r'^$',views.post_lista),
	url(r'^post/(?P<post_pk>[0-9]+)/$',views.post_detalle),
]