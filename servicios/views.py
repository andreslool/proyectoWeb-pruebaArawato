from django.shortcuts import render, HttpResponse
from servicios.models import servicio

# Create your views here.

def servicios(request):

    servicios = servicio.objects.all()

    return render(request, "servicios.html", {"servicios": servicios})