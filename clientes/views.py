from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from django.shortcuts import render

# Create your views here.
def clientes(request):
	if request.user.is_authenticated():
		return render(request, 'clientes/clientes.html', {})
	else:
		return HttpResponseRedirect("/")

def cliente_nuevo(request):
	if request.user.is_authenticated():
		return render(request, 'clientes/nuevo.html', {})
	else:
		return HttpResponseRedirect("/")