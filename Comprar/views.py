from django.shortcuts import render, redirect
import requests
import json
from .forms import *
from .models import *

# Create your views here.

#funcion para obtener la llave:
def getToken():
	linkApi='https://sandbox.wompi.co/v1/merchants/pub_test_cGxmM15rlloTomLxw3eRG7TI0cpzzrFf'
	token = requests.get(linkApi)
	token = token.json()
	
	token = token['data']
	token = token['presigned_acceptance']
	token = token['acceptance_token']

	return token

def GuardarBaseDatosUser(nombre,email,token,plan,metodo):
	user = Pago(nombreApellidos = nombre, email = email, token = token, plan = plan, metodo = metodo)
	user.save()

#Pagina principal
def home(request):
	return render(request, 'home.html')

#Tokens
def token_basic(request):
	token = getToken()

	return redirect(f'CompraBasic/{token}')


def token_normal(request):
	token = getToken()

	return redirect(f'CompraNormal/{token}')


def token_premiun(request):
	token = getToken()

	return redirect(f'CompraPremiun/{token}')


#Pagina de compras
def CompraBasic(request, token):
	if request.method == "GET":
		return render(request, 'CompraBasic.html', {"Formulario":FormDatosUser()})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Basico"
		metodo = request.POST["metodo"]
		monto = "2000000"

		GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiBasic/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}')


def CompraNormal(request, token):
	if request.method == "GET":
		return render(request, 'CompraNormal.html', {"Formulario":FormDatosUser()})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Normal"
		metodo = request.POST["metodo"]
		monto = "4000000"

		GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiNormal/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}')

def CompraPremiun(request, token):
	if request.method == "GET":
		return render(request, 'CompraPremiun.html', {"Formulario":FormDatosUser()})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Premiun"
		metodo = request.POST["metodo"]
		monto = "6000000"

		GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiPremiun/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}')

#Paginas de pago

def pagoNequi(request, nombre, email,token,plan,metodo,monto):
	if request.method == "GET":
		return render(request, 'pagoNequi.html', {"formulario":FormPagoNequi()})