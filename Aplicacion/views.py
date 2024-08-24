import ast
from urllib import request
from weakref import ref
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Curso, Entregable, Profesor, Estudiante
from Aplicacion.forms import cursoFormulario, Buscar, estudiantesForm, profesorFormulario, entregablesForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'AplicacionTemplates/padre.html')
def cursos(request):
    return render(request, 'AplicacionTemplates/cursos.html')
def profesores(request):
    return render(request,'AplicacionTemplates/profesores.html')
def estudiantes(request):
   return render(request,'AplicacionTemplates/estudiantes.html')
def entregables(request):
    return render(request,'AplicacionTemplates/entregables.html')



def curso_form(request): 
    if request.method == "POST":
        
        CursoFormulario = cursoFormulario(request.POST)  # Aquí llega la información del HTML
        print(CursoFormulario)
        if CursoFormulario.is_valid():  # Asegúrate de usar los paréntesis aquí
            informacion = CursoFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render(request,"AplicacionTemplates/index.html") 
    else:
        # Si el request es GET, muestra un formulario vacío
        CursoFormulario = cursoFormulario()
        return render(request, "AplicacionTemplates/cursoFormulario.html", {"CursoFormulario": CursoFormulario})
    
def profesor_formulario(request):
    if request.method == "POST":
        prof_formulario = profesorFormulario(request.POST)  # Usa el nombre correcto de la clase de formulario
        print(prof_formulario)
        if prof_formulario.is_valid():
            informacion = prof_formulario.cleaned_data
            profesor = Profesor(
                nombre=informacion["nombre"],
                apellido=informacion["apellido"],
                email=informacion["email"],
                profesion=informacion["profesion"]
            )
            profesor.save()
            return render(request, "AplicacionTemplates/index.html")
    else:
        prof_formulario = profesorFormulario()  # Usa el nombre correcto de la clase de formulario
    
    return render(request, "AplicacionTemplates/profesorForm.html", {"prof_formulario": prof_formulario})

def estudiantes_Formulario(request):
    
    if request.method == "POST":
    
        EstFormulario = estudiantesForm(request.POST)
        print(EstFormulario)
        
        if EstFormulario.is_valid():
            informacion = EstFormulario.cleaned_data
            estudiante = estudiantes(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()  
            return render(request, "AplicacionTemplates/index.html")  
    else:
        EstFormulario = estudiantesForm()
        return render(request, "AplicacionTemplates/estudiantesForm.html", {"EstFormulario": EstFormulario})

def entregables_Formulario(request):
    if request.method == "POST":
        entre_formulario = entregablesForm(request.POST)  # Usa el nombre correcto de la clase de formulario
        print(entre_formulario)
        if entre_formulario.is_valid():
            informacion = entre_formulario(request)
            entregable = Entregable( nombre=informacion["nombre"],fecha_entrega=informacion["fecha_entrega"]   )
            entregable.save()
            return render(request, "AplicacionTemplates/index.html")
    else:
        entre_formulario = entregablesForm()  # Asegúrate de que esta línea se ejecute siempre en un GET

    return render(request, "AplicacionTemplates/entregableForm.html", {"entre_formulario": entre_formulario})
 
def buscar (request):
 if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        camada = camada.objects.filter(nombre__icontains=nombre)
        return render(request, "AplicacionTemplates/resultadoBusqueda.html", {"camada": camada, "nombre": nombre})
 else: 
       respuesta = "No enviaste datos"
     
       return HttpResponse(respuesta)
    