from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField()
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Camada: {self.camada}"

class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email: {self.email}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)
    def __str__(self) -> str:
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - Email:{self.email} - profesion: {self.profesion}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=30)   
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()   
    
    def __str__(self) -> str:
        return f"nombre: {self.nombre} - fecha_de_entrega: {self.fecha_de_entrega} - entregado: {self.entregado}"
