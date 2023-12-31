from django.urls import path
from .views import *

CortLinkBasic = "token_basic/CompraBasic/"
CortLinkNormal = "token_normal/CompraNormal/"
CortLinkPremiun = "token_premiun/CompraPremiun/"

CortLinkNequiBasic = "pagoNequiBasic/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"
CortLinkNequiNormal = "pagoNequiNormal/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"
CortLinkNequiPremiun = "pagoNequiPremiun/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"

CortLinkTarjetaBasic = "pagoTarjetaBasic/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"
CortLinkTarjetaNormal = "pagoTarjetaNormal/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"
CortLinkTarjetaPremiun = "pagoTarjetaPremiun/<str:nombre>/<str:email>/<str:token>/<str:plan>/<str:metodo>/<int:monto>/<str:referencia>/"
urlpatterns = [
	path('', home, name = 'home'),
	
	#Paginas para obtener tokens
	path('token_basic/', token_basic, name = 'token_basic'),
	path('token_normal/', token_normal, name = 'token_normal'),
	path('token_premiun/', token_premiun, name = 'token_premiun'),

	#Paginas de formulario de pagos
	path('token_basic/CompraBasic/<str:token>', CompraBasic, name = 'CompraBasic'),
	path('token_normal/CompraNormal/<str:token>', CompraNormal, name = 'CompraNormal'),
	path('token_premiun/CompraPremiun/<str:token>', CompraPremiun, name = 'CompraPremiun'),

	#Paginas de metodo de pago Nequi
	path(f'{CortLinkBasic}{CortLinkNequiBasic}', pagoNequi, name = "PagoNequiBasic"),
	path(f'{CortLinkNormal}{CortLinkNequiNormal}', pagoNequi, name = "PagoNequiNormal"),
	path(f'{CortLinkPremiun}{CortLinkNequiPremiun}', pagoNequi, name = "pagoNequiPremiun"),

	#Paginas de metodo de pago Tarjeta
	path(f'{CortLinkBasic}{CortLinkTarjetaBasic}', pagoTarjeta, name = "PagoTarjetaBasic"),
	path(f'{CortLinkNormal}{CortLinkTarjetaNormal}', pagoTarjeta, name = "PagoTarjetaNormal"),
	path(f'{CortLinkPremiun}{CortLinkTarjetaPremiun}', pagoTarjeta, name = "pagoTarjetaPremiun"),
]