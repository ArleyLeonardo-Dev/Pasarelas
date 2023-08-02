from django.shortcuts import render, redirect
import requests
import json
from .forms import *

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
	return render(request, 'CompraBasic.html', {"Formulario":FormDatosUser()})


def CompraNormal(request, token):
	return render(request, 'CompraNormal.html', {"Formulario":FormDatosUser()})


def CompraPremiun(request, token):
	return render(request, 'CompraPremiun.html', {"Formulario":FormDatosUser()})