from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
import requests

# variables
APIurl = 'http://127.0.0.1:8000/API/JWT/'
# Create your views here.

def cerrarSeccion(request):
    del request.session['jwts']
    del request.session['logout']
    return redirect('home')

def inicioSeccion(request):
    if request.method == 'GET':
        validacion = 0
        return render(request, 'inicioSeccion.html', {'formulario': AuthenticationForm(), 'validacion':validacion})
    else:
        try:
            username = request.POST["username"]
            GetUser = User.objects.get(username = username)
            
        except:
            validacion = 1
            return render(request, 'inicioSeccion.html', {'formulario': AuthenticationForm(), 'validacion':validacion})
        
        if request.POST["password"] != GetUser.password:
            validacion = 2
            return render(request, 'inicioSeccion.html', {'formulario': AuthenticationForm(), 'validacion':validacion})
        else:
            id = GetUser.id 
            username = GetUser.username
            password = GetUser.password
            
            payload = {
                'id':id,
                'username':username,
                'password':password
            }
            jwtToken = requests.post(APIurl,json=payload)
            jwtToken = jwtToken.json()
            jwtToken = jwtToken['JWT']
            
            request.session['jwts'] = jwtToken
            request.session['logout'] = 'autenticado'
            request.session.save()
            return redirect('home')

    
def registroSeccion(request):
    if request.method == 'GET':
        
        validacion = 0
        return render(request, 'registroSeccion.html', {'formulario': UserCreationForm(),'validacion':validacion})
    else:
        try:
            username = request.POST["username"]
            GetUser = User.objects.get(username = username)
            
        except:
            if request.POST["password1"] != request.POST["password2"]:
                validacion = 1
                return render(request, 'registroSeccion.html', {'formulario': UserCreationForm(),'validacion':validacion})
            else:
                username = request.POST["username"]
                password = request.POST["password1"]
                
                crearUser = User(username = username, password = password)
                crearUser.save()
                
                return redirect('inicioSeccion')
            
        validacion = 2
        return render(request, 'registroSeccion.html', {'formulario': UserCreationForm(),'validacion':validacion})