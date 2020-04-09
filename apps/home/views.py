from django.shortcuts import render

from django.views.generic import (
    TemplateView,
    ListView,
)

class IndexView(TemplateView):
    #una vista procesa los datos y renderiza el resultado en pantalla, siempre nos pedirá un template para trabajar
    #Un template es un archivo HTML
    template_name = "home/index.html"
    
class ListaLibros(ListView):
    template_name = "home/libros.html"
    queryset = {"El quijote de la mancha", "Codigo limpio", "La sombra del viento", "Django 2.0"}
    context_object_name = "libros"

# Create your views here.
