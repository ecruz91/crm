from django.contrib import auth
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template.loader import get_template
from .forms import UserLoginForm

def home(request):
	if request.user.is_authenticated():
		return render(request, 'index/index.html', {})
	else:
		return HttpResponseRedirect("/login/")

def login_crm(request):
	if request.user.is_authenticated():
		return HttpResponseRedirect("/")
	else:
		form = UserLoginForm(request.POST or None)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(username=username, password=password)
			login(request, user)
			return HttpResponseRedirect("/")
		return render(request, 'auth/login.html', {"form":form})

def register_crm(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/login/")

def logout_crm(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponseRedirect("/login/")

def handler404(request):
	response = render_to_response('404.html', {}, context_instance = RequestContext(request))
	response.status_code = 404
	return response