from django.shortcuts import redirect
from django.conf import settings
import jwt
from django.contrib.auth.models import User

def decodificarJWT(TokenJwt):
    secretKey = settings.SECRET_KEY
    algorithm='HS256'
    try:
        datos = jwt.decode(TokenJwt,secretKey,algorithms=algorithm)
    except jwt.ExpiredSignatureError:
        return 'Token expired'
    return datos


class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path == '/':
            response = self.get_response(request)
        elif request.path == '/Seccion/':
            response = self.get_response(request)
        elif request.path == '/API/JWT/':
            response = self.get_response(request)
        else:
            if request.session.get('jwts',None) == None:
                return redirect('inicioSeccion')
            else:
                token = decodificarJWT(request.session['jwts'])
                try:
                    id = token["id"]
                    user = User.objects.get(id = id)
                    response = self.get_response(request)
                except:
                    return redirect('home')
                   
        return response