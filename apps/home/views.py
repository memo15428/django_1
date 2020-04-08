from django.shortcuts import render

from django.views.generic import (
    TemplateView,
)

class IndexView(TemplateView):
    print("---------------------prueba de URL-------------------------")

# Create your views here.
