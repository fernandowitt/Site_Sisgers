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
	return render(request, 'relatorios/lista_vistorias.html', {'vistorias':vistorias})