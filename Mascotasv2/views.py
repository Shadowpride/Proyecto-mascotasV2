from django.shortcuts import render
from django.http import HttpResponse

def hola(request):
    return render(request,"hola.html")

def chau(request):
    return render(request,"chau.html")