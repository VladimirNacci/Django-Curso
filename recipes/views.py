from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_view(request):
    return render(request, 'recipes/home.html')


def contato_view(request):
    return render(request, 'recipes/contato.html')


def sobre_view(request):
    return render(request, 'recipes/sobre.html')
