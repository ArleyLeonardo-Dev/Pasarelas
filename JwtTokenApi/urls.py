from django.urls import path
from .views import *

urlpatterns = [
    path('Ingresar/', Ingresar.as_view() , name = 'Ingresar'),
    path('Registrar/', Registrar.as_view(), name = 'Registrar')
]