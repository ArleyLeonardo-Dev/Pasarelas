from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from django.conf import settings
import jwt

# Create your views here.

class JwtApiView(APIView):
    
    def get(self, request):
        data = {'mensaje':'Digite los datos en el Body'}
        return Response(data,status=status.HTTP_200_OK)
    def post(self, request):
        datosEnviados = request.data
        
        id = datosEnviados['id']
        username = datosEnviados['username']
        password = datosEnviados['password']
        
        payload = {
            'id':id,
            'username':username,
            'password':password,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1)
        }
        secret_key = settings.SECRET_KEY
        algorithm='HS256'
        
        JWTtoken = jwt.encode(payload,secret_key,algorithm)
        
        data = {"JWT":JWTtoken}
        
        return Response(data,status=status.HTTP_200_OK)