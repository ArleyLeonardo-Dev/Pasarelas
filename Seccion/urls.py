from django.urls import path
from .views import *


urlpatterns = [
    path('', inicioSeccion, name = 'inicioSeccion'),
    path('Registro/', registroSeccion, name='registroSeccion'),
    path('cerrarSeccion/', cerrarSeccion, name = 'cerrarSeccion')
]
