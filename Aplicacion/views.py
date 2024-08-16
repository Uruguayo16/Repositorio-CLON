from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

def inicio(req):
    return HttpResponse('vista inicio')

def cursos(req):
    return HttpResponse('vista cursos')

def profesores(req):
    return HttpResponse('vista profesores')

def estudiantes(req):
    return HttpResponse('vista estudiantes')

def entregables(req):
    return HttpResponse('vista entregables')


