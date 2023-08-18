from django.shortcuts import render, redirect
import requests
import json
from .forms import *
from .models import *

# Variables
terminosYcondiciones = "https://wompi.com/assets/downloadble/TC-Usuarios-Colombia.pdf"


## funcion para obtener la llave:
def getToken():
	linkApi='https://sandbox.wompi.co/v1/merchants/pub_test_cGxmM15rlloTomLxw3eRG7TI0cpzzrFf'
	token = requests.get(linkApi)
	token = token.json()
	
	token = token['data']
	token = token['presigned_acceptance']
	token = token['acceptance_token']

	return token


## Funciones para guardar datos en la base de datos
def GuardarBaseDatosUser(nombre,email,token,plan,metodo):
	user = Pago(nombreApellidos = nombre, email = email, token = token, plan = plan, metodo = metodo)
	user.save()
	referencia = user.id

	return f"{referencia}"


def GuardarBaseDatosNequi(token, numero):
	usuario = Pago.objects.get(token = token)
	nequi = DatosNequi(usuario = usuario, numero = numero)
	nequi.save()


def GuardarBaseDatosTarjeta(token, idTransaccion):
	usuario = Pago.objects.get(token = token)
	tarjeta = DatosTarjeta(usuario = usuario, IdTransaccion = idTransaccion)
	tarjeta.save()


#Funciones para hacer llamado a las APIs
def postAPI(lista):
	linkApi = 'https://sandbox.wompi.co/v1/transactions'
	header = {"Authorization":'Bearer prv_test_rWOEDvkLHehCZVPaGXdEbFYmWmOelF2U'}

	transaccion = requests.post(linkApi, headers = header, json = lista)

	transaccion = transaccion.json()
	print(transaccion)
	transaccion = transaccion["data"]
	transaccion = transaccion["id"]

	return transaccion


def tokenizarTarjeta(lista):
	linkApi = 'https://sandbox.wompi.co/v1/tokens/cards'
	header = {"Authorization":'Bearer pub_test_cGxmM15rlloTomLxw3eRG7TI0cpzzrFf'}

	tokenizar = requests.post(linkApi, headers = header, json = lista)

	tokenizar = tokenizar.json()
	tokenizar = tokenizar["data"]
	tokenizar = tokenizar["id"]

	return tokenizar


def crearFuentePago(lista):
	linkApi = 'https://sandbox.wompi.co/v1/payment_sources'
	header = {"Authorization":'Bearer prv_test_rWOEDvkLHehCZVPaGXdEbFYmWmOelF2U'}

	idFuentePago = requests.post(linkApi, headers = header, json = lista)

	idFuentePago = idFuentePago.json()
	idFuentePago = idFuentePago["data"]
	idFuentePago = idFuentePago["id"]

	return idFuentePago


#Pagina principal
def home(request):
    try:
        autenticado = request.session['logout']
        return render(request, 'home.html',{"autenticado":autenticado})
    except:
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
		try:
			autenticado = request.session['logout']
			return render(request, 'CompraBasic.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones, 'autenticado':autenticado})
		except:
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
		elif metodo == "Tarjeta":
			return redirect(f'pagoTarjetaBasic/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')


def CompraNormal(request, token):
	if request.method == "GET":
		try:
			autenticado = request.session['logout']
			return render(request, 'CompraNormal.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones, 'autenticado':autenticado})
		except:
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
		elif metodo == "Tarjeta":
			return redirect(f'pagoTarjetaNormal/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')

def CompraPremiun(request, token):
	if request.method == "GET":
		try:
			autenticado = request.session['logout']
			return render(request, 'CompraPremiun.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones, 'autenticado':autenticado})
		except:
			return render(request, 'CompraPremiun.html', {"Formulario":FormDatosUser(),"Terminos":terminosYcondiciones})
	else:
		nombre = request.POST["usuario"]
		email = request.POST["correo"]
		token = token
		plan = "Premiun"
		metodo = request.POST["metodo"]
		monto = 6000000
		referencia = GuardarBaseDatosUser(nombre,email,token,plan,metodo)

		if metodo == "Nequi":
			return redirect(f'pagoNequiPremiun/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')
		elif metodo == "Tarjeta":
			return redirect(f'pagoTarjetaPremiun/{nombre}/{email}/{token}/{plan}/{metodo}/{monto}/{referencia}')

#Paginas de pago

def pagoNequi(request, nombre, email,token,plan,metodo,monto,referencia):
	if request.method == "GET":
		try:
			autenticado = request.session['logout']
			return render(request, 'pagoNequi.html', {"formulario":FormPagoNequi(), "plan":plan, 'autenticado':autenticado})
		except:
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
		idTransaccion = postAPI(lista)

		try:
			autenticado = request.session['logout']
			return render(request, "confirmacion.html", {"Plan":plan, 'autenticado':autenticado})
		except:
			return render(request, "confirmacion.html", {"Plan":plan})

def pagoTarjeta(request, nombre, email,token,plan,metodo,monto,referencia):
	if request.method == "GET":
		try:
			autenticado = request.session['logout']
			return render(request, 'pagoTarjeta.html', {"formulario":FormPagoTarjeta(), "plan":plan, 'autenticado':autenticado})
		except:
			return render(request, 'pagoTarjeta.html', {"formulario":FormPagoTarjeta(), "plan":plan})
	else:
		numero = request.POST["numero"]
		cvc = request.POST["cvc"]
		exp_mes = request.POST["exp_mes"]
		exp_year = request.POST["exp_year"]
		nombre = request.POST["nombre"]

		listaTokenizar = {
			"number":numero,
			"cvc":cvc,
			"exp_month":exp_mes,
			"exp_year":exp_year,
			"card_holder":nombre
		}

		tokenTarjeta = tokenizarTarjeta(listaTokenizar)

		listaCrearFuentePago = {
			"type":"CARD",
			"token":tokenTarjeta,
			"customer_email":email,
			"acceptance_token":token 
		}

		idFuentePago = crearFuentePago(listaCrearFuentePago)

		listaTransaccion = {
			"amount_in_cents": monto,
			"currency": "COP",
			"customer_email":email,
			"payment_method":{"installments":1},
			"reference":referencia,
			"payment_source_id":idFuentePago
		}

		idTransaccion = postAPI(listaTransaccion)

		GuardarBaseDatosTarjeta(token, idTransaccion)

		try:
			autenticado = request.session['logout']
			return render(request, "confirmacion.html", {"Plan":plan, 'autenticado':autenticado})
		except:
			return render(request, "confirmacion.html", {"Plan":plan})





