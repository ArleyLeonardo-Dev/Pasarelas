from django.shortcuts import render, redirect

# Create your views here.


def home(request):
	
	return render(request, 'home.html')

#Tokens
def token_basic(request):

	return redirect('CompraBasic/')


def token_normal(request):

	return redirect('CompraNormal')

def token_premiun(request):

	return redirect('CompraPremiun')


#Pagina de compras
def CompraBasic(request):

	return render(request, 'CompraBasic.html')


def CompraNormal(request):

	return render(request, 'CompraNormal.html')


def CompraPremiun(request):

	return render(request, 'CompraPremiun.html')