from django.http import HttpResponse
from .models import Usuario
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.models import User,AbstractBaseUser, BaseUserManager
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib import messages

usuario_creado = bool
usuario_datos=[]

def index(request):
    return render(request,"index.html")
    
def tienda(request):
    return render(request,"tienda.html")

def olvidaste(request):
    return render(request, "olvidaste.html")

@csrf_protect
def procesar_formulario(request):
    if request.method == 'POST':
        contra = request.POST.get('contraseña')
        correo = request.POST.get('correo')
        a=request.POST.get("submit_action")
        if (a=="entrar"):
            return verificar_usuario(request,correo, contra)
        else:
            return redirect('registrar')


def registrar(request):
    return render(request, 'registrar.html')

@csrf_protect
def procesar_formulario2(request):
    if request.method == 'POST':
        contraseña = request.POST.get('contraseña')
        correo = request.POST.get('correo')
        telefono = request.POST.get('tel')
        nombre = request.POST.get('nombre')
        nacimineto = request.POST.get('nacimiento')
        a=request.POST.get("submit_action")
        if (a=="entrar"):
            try:
                user=Usuario(name=nombre, password=contraseña, gmail=correo, number=telefono, date=nacimineto)
                user.save()
                usuario_creado = True
            except IntegrityError:
                usuario_creado = False
        
        if (usuario_creado==True):
                b="Usurio creado con exito, inicie secion para continuar"
                c="Felicidades"
                img="check.png"
                print(b)
                return render(request, 'nuevosUsuarios.html/', {'usuario_creado': b, "felicidades":c, "img":img})
        else:
            b="El usuario no se puedo crear"
            c="Error"
            img="error.png"
            print(b)
            return render(request, 'nuevosUsuarios.html/', {'usuario_creado': b, "felicidades":c,"img":img})
    
def buy(request):
    return render(request, "buy.html")

def infomacion(request):
    return render(request, "info.html")

def contacto(request):
    b=request.session.get("my_data")
    return render(request, "contacto.html", {"nombre": b[0],"contra":b[1],"gmail":b[2],"numero":b[3],"fecha":b[4]})


def datos(request):
        datos=usuario_datos[0]
        userio=Usuario.objects.get(name=datos)
        nombre=userio.name
        contra=userio.password
        correo=userio.gmail
        numero=userio.number
        date=userio.date
        return (nombre,contra,correo,numero,date)
    

def trabajo(request):
    return render(request, "trabajo.html")

def verificar_usuario(request, gmail, contra):
    try:
        usuario = Usuario.objects.get(gmail=gmail)
        return verificar_contraseña(request,contra)
    except Usuario.DoesNotExist:
        messages.error(request, 'El correo electrónico proporcionado no existe.')
        return render(request,"index.html")

def verificar_contraseña(request, contra):
    try:
        usuario = Usuario.objects.get(password=contra)
        usuario_datos.append(usuario)
        f= datos(request)
        request.session['my_data'] = f
        return redirect('tienda')
    except Usuario.DoesNotExist:
        messages.error(request, 'Las contraseñas no coinciden.')
        return render(request,"index.html")


def procesar_formulario3(request):
    if request.method == 'POST':
        contra = request.POST.get('contraseña')
        correo = request.POST.get('correo')
        a=request.POST.get("submit_action")
        print(contra,correo,a)
        if (a=="registrar"):
            if contra==correo:
                return (verificar_usuario2(request,contra))
            else:
                messages.error(request,'La contraseña proporcionado no existe.')
                return contacto(request)

def verificar_usuario2(request,contra):
    try:
        b=request.session.get("my_data")
        usuario = Usuario.objects.get(name=b[0])
        usuario.password= contra
        usuario.save()
        return contacto(request)
    except:
        return contacto(request)
    
def finalizar(request):
    return render(request, "finalizar.html")