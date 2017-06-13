# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from .models import *
from .forms import *




# Blogue Views
def blog(request):
    Artigos = Artigo.objects.filter(status='p').order_by('-data')
    return render(request, 'Blog/blog.html', {
        'main': 'home',
        'pagina': 'Blog',
        'artigos': Artigos,
    })



def artigo(request, titulo):
    a = titulo.replace('-', ' ').title()

    try:
        artigo = Artigo.objects.get(titulo=titulo)

        if request.user.is_authenticated:
            auth = True
        else:
            auth = False

    except Artigo.DoesNotExist:
        raise Http404('Hmmm, artigo {} não exite!'.format(titulo))
    return render(request, 'Blog/artigo.html', {
        'auth': auth,
        'main': 'blog',
        'pagina': 'Blog',
        'titulo': titulo,
        'artigo': artigo,
        'autor': artigo.autor,
        'imagem_do_autor': artigo.autor.perfil.url,
        #'imagem_do_artigo': artigo.imagem.url,
        'data': artigo.data,
        'conteudo': artigo.artigo,
    })



def artigo_add(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = ArtigoForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.save()
                return redirect('/blog/')
        else:
            form = ArtigoForm()
        return  render(request, 'Blog/artigo-add.html',{
            'main': 'blog',
            'pagina': 'Novo',
            'form': form,
        })
    else:
        return render(request, '401.html',{
            'pagina': '401',
        })




def autor(request):
    return render(request, 'Blog/autor.html',{
        'main': 'blog',
        'pagina': 'Autor',
    })


def doautor(request, autor):
    p = Pessoa.objects.get(nome=autor)
    relacionados = Artigo.objects.filter(autor=p).order_by('-data')
    return render(request, 'Blog/doautor.html',{
        'main': 'blog',
        'pagina': 'Artigos',
        'autor': autor,
        'artigos': relacionados,
        'pessoa': p,
    })


#####################################################