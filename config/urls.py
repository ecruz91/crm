from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^clientes/', include('clientes.urls')),
	url(r'^login/', views.login_crm, name='login'),
	url(r'^logout/', views.logout_crm),
	url(r'^admin/', admin.site.urls),
]
