from django.urls import path
from Aplicacion import views
from Aplicacion import views_clases


<<<<<<< HEAD
urlpatterns =   [

    
    path('inicio/', views.inicio, name="inicio"),
    path('cursos/', views.cursos, name="cursos"),    
    path('profesores/', views.profesores, name="profesores"),
    path('estudiantes/', views.estudiantes, name="estudiantes"),
    path('entregables/', views.entregables, name="entregables"),
    path('curso-form/', views.curso_form, name="CursoFormulario"), 
    path('profe-form/', views.profesor_formulario, name="prof_formulario"),
    path('estudiantes-form/', views.estudiantes_Formulario, name="EstFormulario"),
    path('entregables-form/', views.entregables_Formulario, name="EntreFormulario"),
    path('buscar/', views.buscar,name="miFormulario"),
]



urls_vistas_clases = [
    path('clases/lista/', views_clases.CursoListView.as_view(), name='List'),
    path('clases/detalle/<int:pk>/', views_clases.CursoDetailView.as_view(), name='Detail'),
    path('clases/nuevo/', views_clases.CursoCreateView.as_view(), name='New'),
    path('clases/editar/<int:pk>', views_clases.CursoUpdateView.as_view(), name='Edit'),
    path('clases/eliminar/<int:pk>', views_clases.CursoDeleteView.as_view(), name='Delete')
=======
urlpatterns = [
    
    path('inicio/', views.inicio),
    path('cursos/', views.cursos),    
    path('profesores/', views.profesores),
    path('estudiantes/', views.estudiantes),
    path('entregables/', views.entregables),
    path('curso-form/', views.curso_form), 
    path('curso-form-2/', views.curso_form_2,name='CursoForm2'),
    path('profesorFormulario/', views.profesorFormulario),
    path ('buscar/', views.buscar),
    path ('leer_Profesores/', views.leerProfesores),  
    path ('eliminar_Profesor/ <profesor_nombre>/', views.eliminarProfesor), 
    path ('editarProfesor/ <profesor_nombre>/',views.editarProfesor),
>>>>>>> e61fa8e (Cambios)
]