import email
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from Informacion.models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from Informacion.forms import *
from django.template import loader
from django.contrib.auth.decorators import login_required

# Create your views here.

#INICIO
def inicio(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, "padre.html")

#ABOUT
def about(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render (request, "hijo_about.html")

#INICIAR SESION
def login_request(request):

    if request.method == "POST":

        form = AuthenticationForm(request , data= request.POST)

        if form.is_valid():
            
            usuario = form.cleaned_data.get("username")
            contra = form.cleaned_data.get("password")

            user = authenticate(username=usuario , password=contra)

            if user is not None:
                login(request, user)
                avatares = Avatar.objects.filter(user=request.user.id)
                return render( request , "padre.html")
    
            else:
                return HttpResponse(f"Usuario Incorrecto")
        else:         
            return HttpResponse(f"FORM INCORRECTO {form}")

    form = AuthenticationForm()

    return render( request , "hijo_login.html" , {"form":form})

#REGISTRARSE X 1ERA VEZ
def register (request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return render( request , "padre.html")

    else:
        form = UserCreationForm()
        return render (request, "hijo_registro.html" , {"form":form})

#SUBIR ARCHIVOS
def upload(request):

    if request.method == "POST":
        mi_formulario = archivo( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data          
            publicacion= Archivo(nombre=datos['nombre'] , apellido=datos['apellido'], profesion=datos['profesion'], titulo=datos['titulo'] , cuerpo =datos['cuerpo'], fecha=datos['fecha'], adjunto=datos['adjunto'], autor=datos['autor'])
            publicacion.save() 

            publicacion = Archivo.objects.all()  
            avatares = Avatar.objects.filter(user=request.user.id)
            return render(request , "hijo_blog.html" , {"publicacion": publicacion})

    return render( request, "hijo_form.html")

    
#BUSCAR ARCHIVOS
def buscar_archivo(request):
    avatares = Avatar.objects.filter(user=request.user.id)
    return render( request , "hijo_buscar.html")

#MOSTRAR LA BUSQUEDA
def buscar(request):
    if request.GET['titulo']:
        titulo = request.GET['titulo']      
        titulo = Archivo.objects.filter(titulo__icontains = titulo)
        avatares = Avatar.objects.filter(user=request.user.id)
        return render( request , "hijo_resultado_busqueda.html" , {"titulo": titulo})

    else:
        return HttpResponse("Campo vacio")



#RENDERIZAR BLOG
@login_required
def publicacion(request):
    publicacion = Archivo.objects.all()  
    return render(request , "hijo_blog.html" , {"publicacion": publicacion})

#BORRAR
def borrar_publicacion (request, id):
    publicacion = Archivo.objects.get(id=id)
    publicacion.delete()

    publicacion = Archivo.objects.all()
    avatares = Avatar.objects.filter(user=request.user.id)
    return render(request , "hijo_blog.html" , {"publicacion": publicacion})

#EDITAR
def editar(request, id):
    publicacion = Archivo.objects.get(id=id)

    if request.method == "POST":

        mi_formulario = archivo( request.POST )

        if mi_formulario.is_valid():
            datos = mi_formulario.cleaned_data  

            publicacion.nombre =datos['nombre']
            publicacion.apellido =datos['apellido']
            publicacion.profesion =datos['profesion']
            publicacion.titulo =datos['titulo']
            publicacion.cuerpo =datos['cuerpo'] 
            publicacion.fecha =datos['fecha']
            publicacion.adjunto =datos['adjunto']
            publicacion.autor =datos['autor']
            publicacion.save() 

            publicacion = Archivo.objects.all()      
            avatares = Avatar.objects.filter(user=request.user.id)   
            return render(request , "hijo_blog.html" , {"publicacion": publicacion})
    else:
        mi_formulario = archivo(initial={'nombre':publicacion.nombre ,'apellido':publicacion.apellido,'profesion':publicacion.profesion,'titulo':publicacion.titulo, 'cuerpo':publicacion.cuerpo, 'fecha':publicacion.fecha, 'adjunto':publicacion.adjunto, 'autor':publicacion.autor })
    
    return render( request , "hijo_editar.html" , {"mi_formulario":mi_formulario, "publicacion": publicacion})

#EDITAR_PERFIL
@login_required
def editarperfil(request):
    usuario = request.user

    if request.method == "POST":
        
        miFormulario = UserEditForm(request.POST)

        if miFormulario.is_valid():

            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            password = informacion['password1']
            usuario.set_password(password)
            usuario.save()

            avatares = Avatar.objects.filter(user=request.user.id)
            return render( request , "hijo_inicio.html")

    else:
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render( request , "hijo_editar_perfil.html" , {"miFormulario":miFormulario , "usuario":usuario})

def comentario (request):
    
    if request.method == "POST":  #Crea los mensajes para cada pagina individual
        formulario = Mensaje_formulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            datos = formulario.cleaned_data
            mensaje = Mensaje(nombre = datos['nombre'],
                              email = datos['email'],
                              mensaje = datos['mensaje']
                              )
            mensaje.save()
            avatares = Avatar.objects.filter(user=request.user.id)
        else:
            print ("No se envio tu comentario!") 
                                      
    return render (request,'padre.html')