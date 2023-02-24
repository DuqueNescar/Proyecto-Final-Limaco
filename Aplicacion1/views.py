from django.shortcuts import render,redirect
from .models import Curso,Curso1,Curso2  #los models
from .form import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.

########################################

def iniciosesion(request):

    if request.method == "POST":
        
        form = AuthenticationForm(request, data = request.POST)

        if form.is_valid():  # Si pasó la validación de Django

            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username= usuario, password=contrasenia)

            if user :
                login(request, user)

                return render(request, "index.html", {"mensaje":f"Bienvenido {usuario}"})
            

        else:
                return render(request, "index.html", {"mensaje":"Datos incorrectos"})
           
    else:

       

      form = AuthenticationForm()

    return render(request, "login.html", {"formulario": form})

############################################################

def registro(request):

      if request.method == 'POST':

            #form = UserCreationForm(request.POST)
            form = UsuarioRegistro(request.POST)
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"index.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            #form = UserCreationForm()       
            form = UsuarioRegistro()     

      return render(request,"registro.html" ,  {"form":form})

#####################################################

def editarusuario(request):

    usuario = request.user

    if request.method == "POST":

        form = FormularioEditar(request.POST)

        if form.is_valid():

            info = form.cleaned_data

            usuario.email = info["email"]
            usuario.set_password(info["password1"])
            usuario.first_name = info['first_name']
            usuario.last_name = info['last_name']

            usuario.save()

            return render(request, "index.html")
    
    else:

        form = FormularioEditar(initial={

            "email":usuario.email,
            "first_name":usuario.first_name,
            "last_name":usuario.last_name,
        })

    return render(request, "editarperfil.html",{"formulario":form, "usuario":usuario})
           

#################################################
@login_required

def agregaravatar(request):

    if request.method == "POST":

        form = AvatarFormulario(request.POST, request.FILES)

        if form.is_valid():

            usuarioActual = User.objects.get(username=request.user)
            avatar1 = avatar(usuario=usuarioActual, imagen=form.cleaned_data["imagen"])
            avatar1.save()

            return render(request, "index.html")

    else :

            form = AvatarFormulario

    return render(request, "agregaravatar.html" , {"formulario":form})






######################################################


def base(request):

 return render(request,"index.html")


@login_required
def home(request):
    cursoslistados = Curso.objects.all()
    return render(request,"gestioncursos.html",{"cursos":cursoslistados}) #este cursos es el q se pone en el html




def registrarcurso(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['txtcreditos']

    curso = Curso.objects.create(codigo=codigo, nombre=nombre, creditos=creditos)
    return redirect('/')




def edicioncurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request,"edicioncurso.html", {"curso":curso})

def editarcurso(request):
    codigo=request.POST['txtcodigo']
    nombre=request.POST['txtnombre']
    creditos=request.POST['txtcreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nombre = nombre
    curso.creditos = creditos
    curso.save()

    return redirect('/')

def eliminarcurso(request,codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()
    return redirect('/')



####################################################
@login_required
def home1(request):
    cursoslistados1 = Curso1.objects.all()
    return render(request,"gestioncursos1.html",{"curso1":cursoslistados1}) #este cursos es el q se pone en el html

def registrarcurso1(request):
    codigo1=request.POST['txtcodigo1']
    nombre1=request.POST['txtnombre1']
    creditos1=request.POST['txtcreditos1']

    curso1 = Curso1.objects.create(codigo1=codigo1, nombre1=nombre1, creditos1=creditos1)
    return redirect('/registro1')

def edicioncurso1(request,codigo1):
    curso1 = Curso1.objects.get(codigo1=codigo1)
    return render(request,"edicioncurso1.html", {"curso1":curso1})

def editarcurso1(request):
    codigo1=request.POST['txtcodigo1']
    nombre1=request.POST['txtnombre1']
    creditos1=request.POST['txtcreditos1']

    curso1 = Curso1.objects.get(codigo1=codigo1)
    curso1.nombre1 = nombre1
    curso1.creditos1 = creditos1
    curso1.save()

    return redirect('/registro1')


def eliminarcurso1(request,codigo1):
    curso1 = Curso1.objects.get(codigo1=codigo1)
    curso1.delete()
    return redirect('/registro1')

#################################################
@login_required
def home2(request):
    cursoslistados2 = Curso2.objects.all()
    return render(request,"gestioncursos2.html",{"curso2":cursoslistados2}) #este cursos es el q se pone en el html

def registrarcurso2(request):
    codigo2=request.POST['txtcodigo2']
    nombre2=request.POST['txtnombre2']
    creditos2=request.POST['txtcreditos2']

    curso2 = Curso2.objects.create(codigo2=codigo2, nombre2=nombre2, creditos2=creditos2)
    return redirect('/registro2')

def edicioncurso2(request,codigo2):
    curso2 = Curso2.objects.get(codigo2=codigo2)
    return render(request,"edicioncurso2.html", {"curso2":curso2})

def editarcurso2(request):
    codigo2=request.POST['txtcodigo2']
    nombre2=request.POST['txtnombre2']
    creditos2=request.POST['txtcreditos2']

    curso2 = Curso2.objects.get(codigo2=codigo2)
    curso2.nombre2 = nombre2
    curso2.creditos2 = creditos2
    curso2.save()

    return redirect('/registro2')


def eliminarcurso2(request,codigo2):
    curso2 = Curso2.objects.get(codigo2=codigo2)
    curso2.delete()
    return redirect('/registro2')


#######################################
def sobremi(request):

 return render(request,"sobremi.html")