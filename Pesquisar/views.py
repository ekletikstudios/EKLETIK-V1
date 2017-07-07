# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from django.contrib.postgres import *
from Ek.models import *
from Loja.models import *
from Blog.models import *
from Portfolio.models import *


def SearchUsers(nome):
    return "User...."

def SearchArtigos(keyword):
    try:
        titulos = Artigo.objects.filter(status='p').filter(titulo__icontains=keyword)
        artigos = Artigo.objects.filter(status='p').filter(artigo__icontains=keyword)
        if not artigos:
            artigos = Artigo.objects.filter(status='p').filter(autor__nome__contains=keyword)
    except Artigo.DoesNotExist:
        raise Http404('Nada a mostrar')
    return [artigos, titulos]

def SearchPessoas(keyword):
    try:
        pessoas = Pessoa.objects.filter(nome__icontains=keyword)
    except Pessoa.DoesNotExist:
        raise Http404('Nada a mostrar')
    return pessoas

def SearchLivros(keyword):
    try:
        livros = Livro.objects.filter(status='p').filter(titulo__contains=keyword)
        if not livros:
            livros = Livro.objects.filter(status='p').filter(autor__contains=keyword)
    except Livro.DoesNotExist:
        raise Http404('Nada a mostrar')
    return livros

def SearchAlbums(keyword):
    try:
        albums = Album.objects.filter(status='p').filter(titulo__contains=keyword)
        if not albums:
            albums = Album.objects.filter(status='p').filter(faixa__titulo__contains=keyword)
            if not albums:
                albums = Album.objects.filter(status='p').filter(artista__contains=keyword)
                if not albums:
                    albums = Album.objects.filter(status='p').filter(gravadora__contains=keyword)
                    if not albums:
                        albums = Album.objects.filter(status='p').filter(editorial__contains=keyword)
    except Album.DoesNotExist:
        raise Http404('Nada a mostrar')
    return albums


def SearchPortfolio(keyword):
    try:
        projectos = Projecto.objects.filter(status='p').filter(nome__contains=keyword)
        if not projectos:
            projectos = Projecto.objects.filter(status='p').filter(cliente__contains=keyword)
            if not projectos:
                projectos = Projecto.objects.filter(status='p').filter(informacao__contains=keyword)
                if not projectos:
                    projectos = Projecto.objects.filter(status='p').filter(autor__contains=keyword)
    except Projecto.DoesNotExist:
        raise Http404("Sem Projectos")
    return projectos



def SearchContentTypes(pesquisa):
    types = Artigo.objects.all()
    return types



################# Search Views....

def Pesquisar(request):
    return render(request, 'Pesquisar/search.html', {
        'main': 'Pesquisar',
        'pagina': 'Pesquisar',
    })


def Results(request):

    if request.POST:
        r = request.POST['pesquisa']
        erro = False
        artigos = SearchArtigos(r)
        pessoas = SearchPessoas(r)
        livros = SearchLivros(r)
        albums = SearchAlbums(r)
        users = SearchUsers(r)
        # tipos = SearchContentTypes(r)
    else:
        r = 'POST não recebido'
        erro = True
        artigos = ['null', 'null']
        se = 0
        user = 'None'

    return render(request, 'Pesquisar/results.html', {
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