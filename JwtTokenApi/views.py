from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
import jwt
from django.contrib.auth.models import User

# Create your views here.

class Ingresar(APIView):
    
    def get(self, request):
        
        contenido = {
            'username':' ',
            'password':' ',
        }
        data = {'Datos a ingresar':f'{contenido}'}
        return Response(data,status=status.HTTP_200_OK)
    
    def post(self, request):
        datosEnviados = request.data 
        username = datosEnviados['username']
        password = datosEnviados['password']
        
        try:
            usuario = User.objects.get(username = username)
        except:
            mensaje = {"ERROR":"Este usuario No Existe"}
            return Response(mensaje, status=status.HTTP_204_NO_CONTENT)
        
        if password != usuario.password:
            mensaje = {"Error":"Contraseña Incorrecta"}
            return Response(mensaje, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            payload = {
                'username':username,
                'password':password,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
            }
            secret_key = settings.SECRET_KEY
            algorithm='HS256'
            
            JWTtoken = jwt.encode(payload,secret_key,algorithm)
            
            data = {"Mensaje":"User is aunthenticated","JWT":JWTtoken}
            
            return Response(data,status=status.HTTP_200_OK)
    
class Registrar(APIView):
    def get(self, request):
        contenido = {
            'username':' ',
            'password':' ',
            'passwordConfirm' : ''
        }
        data = {'Datos de Registro':f'{contenido}'}
        return Response(data, status=status.HTTP_200_OK)
    def post(self,request):
        try:
            datos = request.data
            datos = datos['username']
            username = datos
            GetUser = User.objects.get(username = username)
            
        except:
            datos = request.data
            password1 = datos['password'] 
            password2 = datos['passwordConfirm']
            if password1 != password2:
                mensaje = {"EROOR":"Contraseñas no son iguales"}
                return Response(mensaje, status=status.HTTP_406_NOT_ACCEPTABLE)
            else:
                username = datos["username"]
                password = datos["password"]
                
                crearUser = User(username = username, password = password)
                crearUser.save()
                
                mensaje = {"Confirmed":"User created"}
                return Response(mensaje, status= status.HTTP_200_OK)

        contenido = {"ERROR":"Usuario Ya autenticado"}
        return Response(contenido,status=status.HTTP_406_NOT_ACCEPTABLE)