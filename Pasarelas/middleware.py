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


links = ['/', '/Seccion/', '/API/Ingresar/', '/API/Registrar/', '/API/Obtener/', '/API/Vista/','/API/CompraNequi/','/API/CompraCard/']
class CustomMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.path in links:
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