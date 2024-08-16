from django.urls import path
from Aplicacion import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('otro_ejemplo/', views.otro_ejemplo, name='otro_ejemplo'),
]