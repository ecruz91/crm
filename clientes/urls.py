from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.clientes, name='clientes'),
    url(r'^nuevo/$', views.cliente_nuevo, name='nuevo')
]