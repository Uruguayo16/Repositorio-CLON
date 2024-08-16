"""
URL configuration for mi_proyecto project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mi_proyecto.views import saludo,otra_vista,dia_de_hoy,muestra_nombre,probando_template,probando_template,agregar_curso

# Esta es la URL que se encuentra en urls.py de mi_proyecto

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('saludo/', saludo),
    path('otra_vista/', otra_vista),
    path ('nombre/<nombre>', muestra_nombre),
    path ('plantilla/', probando_template),
    path ('agregar_curso/<nom>/<cam>/', agregar_curso)
    
]
