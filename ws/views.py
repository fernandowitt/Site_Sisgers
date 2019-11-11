from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .serializers import VistoriaSerializer
from django.contrib.auth import authenticate
from relatorios.models import Vistoria
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.decorators import api_view, permission_classes
import json
from django.core import serializers
from django.contrib.auth.models import User
import reportlab
from reportlab.pdfgen import canvas
from django.http import HttpResponse


def relatorio(request):
	from reportlab.lib.units import cm
	from reportlab.lib.pagesizes import A4
	from textwrap import wrap
	response = HttpResponse(content_type='application/pdf')
	response['Content-Disposition'] = 'attachment; filename=relatorio.pdf'
	p = canvas.Canvas(response, pagesize = A4)
	p.drawCentredString(11*cm, 24*cm, "ESTADO DE SANTA CATARINA")
	p.drawCentredString(11*cm, 23.5*cm, "SECRETARIA DE ESTADO DA DEFESA CIVIL")
	p.drawCentredString(11*cm, 23*cm, "COORDENADORIA REGIONAL DE DEFESA CIVIL")
	p.drawCentredString(11*cm, 20*cm, "RELATÓRIO CIRCUNSTANCIADO Nº           ")
	p.line(6.7*cm, 19.95*cm, 15.5*cm, 19.95*cm)
	p.drawString(4*cm, 18*cm, "Identificação")
	uf = "a"
	municipio = "b"
	coderec = "c"
	p.drawString(4*cm, 17.5*cm, "UF: %s Municipio: %s CODEREC: %s" % (uf,municipio,coderec))
	p.drawString(4*cm, 17*cm, "Tipologia do Desastre")
	cobrade = "a"
	descricao = "b"
	data = "c"
	hora = "c"
	p.drawString(4*cm, 16.5*cm, "COBRADE: %s Descricao: %s Data: %s Hora: %s" % (cobrade,descricao,data, hora))
	descricao = "ajsndjasjdnasjdashjhfsdhbfhjasdhjfsdbfsdhjfbhjasdbhjfbhsdbfhjsdbhjfbhasdbfhbsdhbfhjasdhjfsdfhjbasdfhjsdbhjfbhjsdbfhbsdhfbhsdbfhjsdbfhsdfbsdhjfbsdhjfbsdhjfbsdhbcsbvhbbbbbbbbbbbbbb"
	p.drawString(4*cm, 16*cm, "Descricao: ")
	wraped_text = '<br/>'.join(wrap(descricao, 20)) 
	p.drawString(6*cm, 16*cm, wraped_text)
	p.showPage()
	p.save()
	return response




# Create your views here.
@csrf_exempt
def loginmobile(request):
	if request.method == 'POST':
		name = request.POST['name']
		password = request.POST['password']
		user=authenticate(username=name, password=password)

		data = None
		if user is not None:
			data = {
				"id": user.id,
				"status": 200
			}
		else:
			data = {
				"status": 404
			}
		return JsonResponse(data)



@api_view(['POST', 'GET'])
@permission_classes((permissions.AllowAny,))	
def cadastrovistoria(request):

	if request.method == 'GET':
		vistorias = Vistoria.objects.all()
		serializer = VistoriaSerializer(vistorias, many=True)
		jason = json.dumps(serializer.data)
		print(jason)

		return JsonResponse(jason, safe=False)

	if request.method == 'POST':
		data = json.loads(request.body.decode('UTF-8'))
		user = User.objects.get(id = data.get('autor'))
		serializer = VistoriaSerializer(data=data)
		if serializer.is_valid():
			print(serializer)
			serializer.save()
			data = {
				"status": 200
			}
			return JsonResponse(data)
		return JsonResponse(serializer.errors, status=400)
