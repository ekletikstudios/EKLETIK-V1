# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals
from django.http import HttpRequest
from django.shortcuts import render, redirect
from Blog.models import *
from Portfolio.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from Serializers import *

#####################################################


def error_404(request):
    origem = request.get_full_path()
    return render(request, '404.html',{
        'origem': origem,
        'pagina': '404',
    })

def Erro(request):
    if request.user.is_authenticated:
        return redirect('/door/')
    origem = request.get_full_path()
    return render(request, '404.html',{
        'origem': origem,
        'pagina': '404',
    })

def Brevemente(request):
    return render(request, '100.html',{
        'pagina': request.path.strip('/'),
    })

def home(request):
    Projectos = Projecto.objects.filter(destaque=True).order_by('-data')
    artigos = Artigo.objects.filter(status='p').order_by('-data')
    Artigos = artigos.filter(destaque=True)
    Pessoas = Pessoa.objects.all()
    return render(request, 'Ek/ek.html', {
        'main': 'home',
        'pagina': 'Ekletik',
        'projectos': Projectos,
        'artigos': Artigos,
        'pessoas': Pessoas,
    })

def empresa(request):
    return render(request, 'Ek/empresa.html', {
        'main': 'home',
        'pagina': 'Empresa',
    })

def contacto(request):
    #c = request.get_signed_cookie(csrftoken)
    req = HttpRequest()
    r = req.META
    path = request.get_full_path()
    other = request.path_info
    return render(request, 'Ek/contacto.html',{
        'main': 'home',
        'pagina': 'Contacto',
        'referer': r,
        'path': path,
        'other': other,
    })

def pedido(request):
    return render(request, 'Ek/pedido.html', {
        'main': 'portfolio',
        'pagina': 'Projectos',
    })


#####################################################


# API Views...
class PessoaListAPI(APIView):
    def get(self, request):
        pessoa = Pessoa.objects.all().filter(status='p').order_by('id')
        serializer = PessoaSerializer(pessoa, many=True)
        return Response(serializer.data)

    def post(self):
        pass