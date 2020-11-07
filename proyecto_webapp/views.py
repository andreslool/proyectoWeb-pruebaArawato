from django.shortcuts import render, HttpResponse

# Create your views here.

def home(request):

    return render(request, "home.html")

def tienda(request):

    return render(request, "tienda.html")

def contacto(request):

    return render(request, "contacto.html")

def politica(request):

   return render(request, "politica.html")

def aviso_legal(request):

    return render(request, "aviso_legal.html")

def cookies(request):

    return render(request, "cookies.html")