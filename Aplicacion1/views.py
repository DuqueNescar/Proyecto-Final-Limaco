from django.shortcuts import render,redirect
from .models import Curso,Curso1,Curso2  #los models

# Create your views here.




######################################################

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