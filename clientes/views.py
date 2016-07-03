from django.shortcuts import render

# Create your views here.
def clientes(request):
	if request.user.is_authenticated():
		return render(request, 'clientes/clientes.html', {})
	else:
		return HttpResponseRedirect("/login/")

def cliente_nuevo(request):
	if request.user.is_authenticated():
		return render(request, 'clientes/nuevo.html', {})
	else:
		return HttpResponseRedirect("/login/")