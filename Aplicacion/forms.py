from django import forms


# Create your forms here.	
class cursoFormulario (forms.Form):
    curso = forms.CharField(max_length=20)
    camada = forms.IntegerField()
    
class Buscar (forms.Form):
    nombre = forms.CharField(max_length=20)

class camadaForm (forms.Form):
    camada = forms.IntegerField()
    nombre = forms.CharField(max_length=20)
    
class estudiantesForm (forms.Form):
    nombre = forms.CharField(max_length=20)
    apellido = forms.CharField(max_length=20)
    email = forms.EmailField()
    
class profesorFormulario (forms.Form): pass
nombre = forms.CharField(max_length=30)
apellido = forms.CharField(max_length=30)
email = forms.EmailField()
profesion = forms.CharField(max_length=20)

class entregablesForm (forms.Form):
    nombre = forms.CharField(max_length=30)
    fecha_entrega = forms.CharField(max_length=30)