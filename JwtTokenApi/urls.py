from django.urls import path
from .views import *
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    path('Ingresar/', Ingresar.as_view() , name = 'Ingresar'),
    path('Registrar/', Registrar.as_view(), name = 'Registrar'),
    path('Obtener/', TokenObtainPairView.as_view(), name = 'Obtener'),
    path('CompraNequi/', ComprarApiNequi.as_view(), name = "Compra Nequi"),
    path('CompraCard/', ComprarApiTarjeta.as_view(), name = "Compra Tarjeta")
]