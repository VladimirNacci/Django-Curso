# from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return HttpResponse('Está é a home do do App Recipes do meu site Django')


def contato_view(request):
    return HttpResponse('Está é a pagina de contato do App Recipes')


def sobre_view(request):
    return HttpResponse("Está é minha pagina sobre do App Recipes.")
