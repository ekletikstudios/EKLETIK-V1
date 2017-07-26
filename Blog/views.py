# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from .models import *
from .forms import *




# Main Blog view. Shows all articles...
def blog(request):
    Artigos = Artigo.objects.filter(status='p').order_by('-data')
    return render(request, 'Blog/blog.html', {
        'main': 'home',
        'pagina': 'Blog',
        'artigos': Artigos,
    })


# Standard view to show a single article...
def artigo(request, titulo):
    a = titulo.replace('-', ' ').title()
    a = titulo
    try:
        artigo = Artigo.objects.get(titulo=titulo)
        slug = artigo.slug
        if request.user.is_authenticated:
            auth = True
        else:
            auth = False

    except Artigo.DoesNotExist:
        return render(request, '404.html',{
            'origem': titulo,
        })
    return render(request, 'Blog/artigo.html', {
        'auth': auth,
        'main': 'blog',
        'pagina': 'Blog',
        'titulo': titulo,
        'artigo': artigo,
        'autor': artigo.autor,
        'imagem_do_autor': artigo.autor.imagem.url,
        'slug': slug,
        'data': artigo.data,
        'conteudo': artigo.artigo,
        'id': artigo.id,
    })


# A view that returns the Django documentation...
def django(request):
    a = Artigo.objects.get(id=3)
    #return artigo(request, a.titulo)
    return redirect('https://github.com/Ngola/Django-Documentation')


# View to add a new article to the db...
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


# View to show an author's profile... TBF
def autor(request):
    return render(request, 'Blog/autor.html',{
        'main': 'blog',
        'pagina': 'Autor',
    })


# View to show articles by a given author...
def doautor(request, autor):
    p = Pessoa.objects.get(nome=autor)
    relacionados = Artigo.objects.filter(autor=p).order_by('-data').filter(status='p')
    return render(request, 'Blog/doautor.html',{
        'main': 'blog',
        'pagina': 'Artigos',
        'autor': autor,
        'artigos': relacionados,
        'pessoa': p,
    })


#####################################################






# API Views...
class ArtigoListAPI(APIView):
    def get(self, request):
        artigos = Artigo.objects.all().filter(status='p').order_by('data')
        serializer = ArtigoSerializer(artigos, many=True)
        return Response(serializer.data)

    def post(self):
        pass
#end ArtigoListAPI