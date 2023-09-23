from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.parsers import JSONParser
from rest_framework.permissions import IsAuthenticated
from Comprar.views import getToken, postAPI, tokenizarTarjeta, crearFuentePago

# Create your views here.
def getReferencia(nombre):
    usuario = User.objects.get(username = nombre)
    return usuario.id

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

class Ingresar(APIView):
    parser_classes = [JSONParser]
    
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
            mensaje = {"ERROR":"Contraseña Incorrecta"}
            return Response(mensaje, status=status.HTTP_406_NOT_ACCEPTABLE)
        else:
            return Response(get_tokens_for_user(usuario), status.HTTP_200_OK)
    
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
    
class ComprarApiNequi(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        Lista = {"Nombre":" ",
                 "Correo":" ",
                 "Plan": " ",
                 "Numero":" ",
                 "Referencia": " "
                 }
        mensaje = {"Introdusca":f"{Lista}"}
        return Response(mensaje,status=status.HTTP_200_OK)
        
    def post(self,request):
        try:
            datos = request.data
            
            nombre = datos['Nombre']
            correo = datos['Correo']
            plan = datos['Plan']
            numero = datos['Numero']
            token = getToken()
            referencia = datos["Referencia"]
            if plan == "Basic":
                monto = 2000000
            elif plan == "Normal":
                monto = 4000000
            elif plan == "Premiun":
                monto = 6000000
        except:
            mensaje = {"Mensaje": "Dijite Todos los datos requeridos"}
            return Response(mensaje, status.HTTP_204_NO_CONTENT)
        
        lista = {
		"acceptance_token": token,
		"amount_in_cents": monto,
		"currency": "COP",
		"customer_email": correo,
		"reference": str(referencia),
		"payment_method": 
		    {
		        "type": "NEQUI",
		        "phone_number": numero
		    }   
		}
        
        try:
            idTransaccion = postAPI(lista)
        except:
            mensaje = {"mensaje":"aqui esta el error"}
            return Response(mensaje, status.HTTP_200_OK)
        mensaje = {
            "Mensaje":"Compra Aprobada",
            "IdTransaccion":f"{idTransaccion}"
        }
        return Response(mensaje, status.HTTP_200_OK)
    
class ComprarApiTarjeta(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        Lista = {"Nombre":"",
                 "Correo":"",
                 "Plan": "",
                 "Numero_Tarjeta":"",
                 "CVC": "",
                 "exp_month": "",
                 "exp_year": "",
                 "Referencia": ""
                 }
        mensaje = {"Introdusca":f"{Lista}"}
        return Response(mensaje,status=status.HTTP_200_OK)
    
    def post(self,request):
        
        try:
            datos = request.data
            
            nombre = datos["Nombre"]
            correo = datos["Correo"]
            plan = datos["Plan"]
            numero = datos["Numero_Tarjeta"]
            cvc = datos["CVC"]
            exp_month = datos["exp_month"]
            exp_year = datos["exp_year"]
            referencia = datos["Referencia"]
            
        except:
            mensaje = {"ERROR":"Dijite Todos los datos"}
            return Response(mensaje,status=status.HTTP_204_NO_CONTENT)
        
        token = getToken()
        if plan == "Basic":
            monto = 2000000
        elif plan == "Normal":
            monto = 4000000
        elif plan == "Premiun":
            monto = 6000000
            
        listaTokenizar = {
			"number":numero,
			"cvc":cvc,
			"exp_month":exp_month,
			"exp_year":exp_year,
			"card_holder":nombre
		}
        
        tokenTarjeta = tokenizarTarjeta(listaTokenizar)
        
        listaCrearFuentePago = {
			"type":"CARD",
			"token":tokenTarjeta,
			"customer_email":correo,
			"acceptance_token":token 
		}
        
        idFuentePago = crearFuentePago(listaCrearFuentePago)
        
        listaTransaccion = {
			"amount_in_cents": monto,
			"currency": "COP",
			"customer_email":correo,
			"payment_method":{"installments":1},
			"reference":referencia,
			"payment_source_id":idFuentePago
		}
        
        idTransaccion = postAPI(listaTransaccion)
        
        mensaje = {
            "Mensaje":"Compra Aprobada",
            "IdTransaccion":f"{idTransaccion}"
        }
        return Response(mensaje, status.HTTP_200_OK)