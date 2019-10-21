from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from random import *
from django.contrib import messages

from django.core.mail import send_mail, BadHeaderError

from .models import Vistoria

def telainicial(request):
	vistorias = Vistoria.objects.filter(data__lte=timezone.now()).order_by('-data')
	return render(request, 'relatorios/vistorias.html', {'vistorias':vistorias})

@login_required
def minhasvistorias(request):
	vistorias = Vistoria.objects.filter(autor=request.user, data__lte=timezone.now()).order_by('-data')
	return render(request, 'relatorios/minhas_vistorias.html', {'vistorias':vistorias})

def vistoriadetalhes(request, pk):
	vistoria = get_object_or_404(Vistoria, pk=pk)
	if request.user == vistoria.autor:
		can_edit = True
	else:
		can_edit = False
	if request.user.is_superuser:
		can_validate = True
	else:
		can_validate = False
	return render(request, 'relatorios/vistoria_detalhes.html', {'vistoria':vistoria, 'can_edit':can_edit, 'can_validate':can_validate})