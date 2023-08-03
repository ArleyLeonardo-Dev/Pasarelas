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
	referencia = user.id

	return referencia


def postAPI(lista):
	linkApi = 'https://sandbox.wompi.co/v1/transactions'
	header = {"Bearer Token":'prv_test_rWOEDvkLHehCZVPaGXdEbFYmWmOelF2U'}

	transaccion = requests.post(linkApi, headers = header, json = lista)


def GuardarBaseDatosNequi(token, numero):
	usuario = Pago.objects.get(token = token)
	nequi = DatosNequi(usuario = usuario, numero = numero)
	nequi.save()


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

terminosYcondiciones = "https://wompi.com/assets/downloadble/TC-Usuarios-Colombia.pdf"
#Pagina de compras
def CompraBasic(request, token):
	if request.method == "GET":
		return render(request, 'CompraBasic.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Basico"
		metodo = request.POST["metodo"]
		monto = "2000000"
		referencia = GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiBasic/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')


def CompraNormal(request, token):
	if request.method == "GET":
		return render(request, 'CompraNormal.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Normal"
		metodo = request.POST["metodo"]
		monto = "4000000"
		referencia = GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiNormal/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')

def CompraPremiun(request, token):
	if request.method == "GET":
		return render(request, 'CompraPremiun.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Premiun"
		metodo = request.POST["metodo"]
		monto = "6000000"
		referencia = GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiPremiun/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')

#Paginas de pago

def pagoNequi(request, nombre, email,token,plan,metodo,monto,referencia):
	if request.method == "GET":
		return render(request, 'pagoNequi.html', {"formulario":FormPagoNequi(), "plan":plan})
	else:
		numero = request.POST["numero"]
		lista = {
		"acceptance_token": token,
		"amount_in_cents": monto,
		"currency": "COP",
		"customer_email": email,
		"reference": referencia,
		"payment_method": 
		    {
		        "type": "NEQUI",
		        "phone_number": numero
		    }
		    
		}

		GuardarBaseDatosNequi(token,numero)
		postAPI(lista)

		return render(request, "confirmacion.html", {"Plan":plan})