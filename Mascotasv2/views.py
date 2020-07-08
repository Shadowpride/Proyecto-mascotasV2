from django.shortcuts import render
from django.http import HttpResponse

def Inicio(request):
    return render(request,"Inicio.html")

def Adopciones(request):
    return render(request,"Adopciones.html")

def Busquedas(request):
    return render(request,"Busquedas.html")
