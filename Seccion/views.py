from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from django.http import HttpResponse


# Create your views here.
def cerrarSeccion(request):
    logout(request)
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
            request.datos= username
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