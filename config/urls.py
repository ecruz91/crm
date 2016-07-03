from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
	url(r'^$', views.home),
	url(r'^login/', views.login_crm),
	url(r'^logout/', views.logout_crm),
	url(r'^admin/', admin.site.urls),
]
