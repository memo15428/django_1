from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)

class IndexView(TemplateView):
    #una vista procesa los datos y renderiza el resultado en pantalla, siempre nos pedirá un template para trabajar
    #Un template es un archivo HTML
    template_name = "home/index.html"
    

# Create your views here.
