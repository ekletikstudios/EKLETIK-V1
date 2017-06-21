# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from Loja.models import *
from Blog.models import *
from Portfolio.models import *


def SearchUsers(nome):
    return "User...."

def SearchArtigos(titulo):
    try:
        artigos = Artigo.objects.filter(titulo__contains=titulo)
    except Artigo.DoesNotExist:
        raise Http404('Nada a mostrar')
    return artigos

def SearchPessoas(nome):
    try:
        pessoas = Pessoa.objects.filter(nome__contains=nome)
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

def SpotifySearch(request):
    return render(request, 'Pesquisar/search.html', {
        'main': 'Pesquisar',
        'pagina': 'Pesquisar',
    })


def SpotifyResults(request):
    #artigos = Artigo.objects.all()
    #projectos = Projecto.objects.all()

    if request.POST:
        r = request.POST['pesquisa']
        erro = False
        artigos = SearchArtigos(r)
        pessoas = SearchPessoas(r)
        livros = SearchLivros(r)
        albums = SearchAlbums(r)
        user = SearchUsers(r)
    else:
        r = 'POST não recebido'
        erro = True
        se = 0
        user = 'None'

    return render(request, 'Pesquisar/results.html', {
        'main': 'Pesquisar',
        'pagina': 'Pesquisar',
        'r': r,
        'erro': erro,
        'pesquisa': request.POST['pesquisa'],
        'artigos': artigos,
        'pessoas': pessoas,
        'livros': livros,
        'albums': albums,
        'user': user,
    })


#####################################################