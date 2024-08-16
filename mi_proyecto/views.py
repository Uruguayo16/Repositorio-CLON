from django.http import HttpResponse
from datetime import datetime
from django.template import loader
from Aplicacion.models import Curso
def saludo(request):
    return HttpResponse("Hola, mundo!")

def otra_vista(request):
    return HttpResponse("<h1> esto es un titulo</h1>  <p> y esto un parrafo </p> ")

def dia_de_hoy(request):
    hoy = datetime.now()
    return HttpResponse(f"Hoy es: {hoy}")

def probando_template(request):
    nom = "Juan"
    ap = "Perez"
    lista_notas = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    diccionario = {"nombre": nom, "apellido": ap, "hoy": datetime.now(), "notas": lista_notas}

    plantilla = loader.get_template("template1.html")

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

def agregar_curso(request, nom, cam):
    
  curso = Curso(nombre=nom, camada=cam)
  curso.save()
  
  return HttpResponse("Curso Agregado")
