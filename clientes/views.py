from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render

def clientes(request):
	if request.user.is_authenticated():
		users = User.objects.all()
		return render(request, 'clientes/clientes.html', {'users':users})
	else:
		return HttpResponseRedirect("/")

def cliente_nuevo(request):
	if request.user.is_authenticated():
		return render(request, 'clientes/nuevo.html', {})
	else:
		return HttpResponseRedirect("/")