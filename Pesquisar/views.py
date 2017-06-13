# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from django.contrib.postgres import *
from Ek.models import *
from Loja.models import *
from Blog.models import *
from Portfolio.models import *


def SearchUsers(nome):
    return "User...."

def SearchArtigos(titulo):
    try:
        titulos = Artigo.objects.filter(titulo__icontains=titulo)
        artigos = Artigo.objects.filter(artigo__icontains=titulo)
    except Artigo.DoesNotExist:
        raise Http404('Nada a mostrar')
    return [artigos, titulos]

def SearchPessoas(nome):
    try:
        pessoas = Pessoa.objects.filter(nome__icontains=nome)
    except Pessoa.DoesNotExist:
        raise Http404('Nada a mostrar')
    return pessoas

def SearchLivros(titulo):
    try:
        livros = Livro.objects.filter(titulo__contains=titulo)
    except Livro.DoesNotExist:
        raise Http404('Nada a mostrar')
    return livros

def SearchAlbums(titulo):
    try:
        albums = Album.objects.filter(titulo__contains=titulo)
    except Album.DoesNotExist:
        raise Http404('Nada a mostrar')
    return albums





################# Search Views....

def Pesquisar(request):
    return render(request, 'Spotify/search.html',{
        'main': 'Pesquisar',
        'pagina': 'Pesquisar',
    })


def Results(request):
    #artigos = Artigo.objects.all()
    #projectos = Projecto.objects.all()

    if request.POST:
        r = request.POST['pesquisa']
        erro = False
        artigos = SearchArtigos(r)
        pessoas = SearchPessoas(r)
        livros = SearchLivros(r)
        albums = SearchAlbums(r)
        users = SearchUsers(r)
    else:
        r = 'POST não recebido'
        erro = True
        artigos = ['null', 'null']
        se = 0
        user = 'None'

    return render(request, 'Spotify/results.html',{
        'main': 'Pesquisar',
        'pagina': 'Resultados',
        'r': r,
        'erro': erro,
        'pesquisa': request.POST['pesquisa'],
        'artigos': artigos[0],
        'titulos': artigos[1],
        'pessoas': pessoas,
        'livros': livros,
        'albums': albums,
        'users': users,
    })


#####################################################