from django.urls import path
from .views import *

urlpatterns = [
	path('', home, name = 'home'),
	
	#Paginas para obtener tokens
	path('token_basic/', token_basic, name = 'token_basic'),
	path('token_normal/', token_normal, name = 'token_normal'),
	path('token_premiun/', token_premiun, name = 'token_premiun'),

	#Paginas de formulario de pagos
	path('token_basic/CompraBasic/<str:token>', CompraBasic, name = 'CompraBasic'),
	path('token_normal/CompraNormal/<str:token>', CompraNormal, name = 'CompraNormal'),
	path('token_premiun/CompraPremiun/<str:token>', CompraPremiun, name = 'CompraPremiun')
]