<<<<<<< HEAD
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
=======
from urllib import request
from weakref import ref
from django.shortcuts import redirect, render
from .models import Curso, Profesor
from Aplicacion.forms import CursoFormulario
from .forms import Buscar
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
        miFormulario = CursoFormulario(request.POST)  # Aquí llega la información del HTML
        print(miFormulario)

        if miFormulario.is_valid():  # Asegúrate de usar los paréntesis aquí
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()
            return render (request, 'Aplicacion/padre.html')  # Redirige a una URL de éxito, define 'success_url' en tu urls.py
        else:
            miFormulario = curso_form()
            # Si el formulario no es válido, renderiza de nuevo con los errores
            return render(request, "Aplicacion/cursoFormulario.html", {"miFormulario": miFormulario})


def curso_form_2(request):

      if request.method == "POST":

            miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)

            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
                  curso.save()
                  return render(request, "Aplicacion/padre.html")
      else:
            miFormulario = CursoFormulario()
      return render(request, "Aplicacion/curso_formulario_2.html", {"miFormulario": miFormulario})

def busquedaCamada (request):
    return render(request, "Aplicacion/busquedaCamada.html")

def buscar (request):
    if request.method == "POST":
     miFormulario = Buscar(request.POST)
     
    if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"], camada=125)
         
            return render (request,"Aplicacion/resultadoBusqueda.html", {"cursos": cursos})
    else:
       miFormulario = buscar()
       return render (request,"Aplicacion/curso_formulario_2.html",{"miFormulario": miFormulario})
    
def profesorFormulario(request):  
        if request.method == 'POST':
                miFormulario = profesorFormulario(request.POST) 
                print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            profesor = Profesor(nombre=informacion['nombre'], apellido=informacion['apellido'], email=informacion['email'], profesion=informacion['profesion'])
            profesor.save() 
            return render(request, "Aplicacion/padre.html") 
        else:
                    miFormulario = profesorFormulario()
        return render(request, 'Aplicacion/profesorFormulario.html', {"miFormulario": miFormulario})

def eliminarProfesor(request, profesor_nombre):
    profesor = Profesor.objects.get(nombre=profesor_nombre)
    profesor.delete()
    
    profesores = Profesor.objects.all()
    
    contexto = {"profesores": profesores}
    return render(request, "Aplicacion/leerProfesores.html",contexto)
    
def leerProfesores(request):

      profesores = Profesor.objects.all() #trae todos los profesores

      contexto= {"profesores":profesores} 

      return render(request, "AppCoder/leerProfesores.html",contexto)
  
def editarProfesor(request, profesor_nombre):
      profesor = Profesor.objects.get(nombre=profesor_nombre)
      
      if request.method == 'POST':
          miFormulario = profesorFormulario(request.POST)
          print (miFormulario)
          
          if miFormulario.is_valid:
              
              informacion = miFormulario.cleaned_data
              profesor.nombre = informacion['nombre']
              profesor.apellido = informacion['apellido']
              profesor.email = informacion['email']
              profesor.profesion = informacion['profesion']
              
              profesor.save()
              
              return render(request, "Aplicacion/index.html")
          
          else:
              miFormulario= profesorFormulario(initial={'nombre': profesor.nombre, 'apellido':profesor.apellido, 'email': profesor.email,'profesion': profesor.profesion})
              
              return render (request, "Aplicacion/editarProfesor.html",{"miFormulario":miFormulario, "profesor_nombre":profesor_nombre})
          
          
>>>>>>> e61fa8e (Cambios)
    