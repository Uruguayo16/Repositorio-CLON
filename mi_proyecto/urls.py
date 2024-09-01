
from django.contrib import admin
from django.urls import path, include
from Aplicacion import views
from Aplicacion.views import cursos
from mi_proyecto.views import saludo, otra_vista, dia_de_hoy, muestra_nombre, probando_template, agregar_curso
 
# Esta es la URL que se encuentra en urls.py de mi_proyecto

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('Aplicacion/', include('Aplicacion.urls')),
    path('saludo/', saludo),
    path('otra_vista/', otra_vista),
    path ('nombre/<nombre>', muestra_nombre),
    path ('plantilla/', probando_template),
    path ('agregar_curso/<nom>/<cam>/', agregar_curso),
    path ('cursos/', views.cursos),
    path('inicio/', views.inicio),  
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
<<<<<<< HEAD
    path('curso-form/', views.curso_form), 
=======
    path('inicio/curso-form/', views.curso_form), 
    path('curso-form-2/', views.curso_form_2),
>>>>>>> e61fa8e (Cambios)
]
