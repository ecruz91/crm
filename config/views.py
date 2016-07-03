from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template

def home(request):
	if request.user.is_authenticated():
		return render(request, 'base.html', {})
	else:
		return HttpResponseRedirect("/login/")

def login_crm(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	else:
		return render(request, 'log/login.html', {})

def logout_crm(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/login/")

def handler404(request):
	Galerias = Galeria.objects.reverse()[:6]
	response = render_to_response('404.html', {'Galerias': Galerias}, context_instance = RequestContext(request))
	response.status_code = 404
	return response