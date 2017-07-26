# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from .models import *





# Loja Views...
def Loja(request):
    a = Album.objects.all().filter(status='p')
    l = Livro.objects.all().filter(status='p')
    return render(request, 'Loja/loja.html', {
        'main': 'home',
        'pagina': 'Loja',
        'albums': a,
        'livros': l,
        'productos': [a, l],
    })

#############-----------------------------------------------------


def Compra(request, keyword):
    try:
        item = Album.objects.get(titulo=keyword)
    except Album.DoesNotExist:
        try:
            item = Livro.objects.get(titulo=keyword)
        except Livro.DoesNotExist:
            raise Http404('Nada encontrado')



    return render(request, 'Loja/recibo.html',{
        'main': 'loja',
        'pagina': 'Recibos',
        'item': item,
    })


##################################################################



def LojaAlbum(request, album):
    origem = request.get_full_path()
    try:
        item = Album.objects.get(titulo=album)
        faixas = Faixa.objects.filter(album=item)
        tipo = 'album'
        autor = item.artista
        empresa = item.gravadora

    except Album.DoesNotExist:
        erro = 'Álbum não encontrado'
        raise Http404('Erro: {}. Origem {}'.format(erro, origem),{
            'erro': erro,
            'origem': origem,
        })

    return render(request, 'Loja/album.html', {
        'item': item,
        'capa': item.capa.url,
        'autor': autor,
        'tamanho': item.ficheiro.size,
        'empresa': empresa,
        'titulo': item.titulo,
        'faixas': faixas.order_by('numero'),
        'pagina': 'Álbum',
        'main': 'loja',
    })



#############################-------------------------------------



def LojaLivro(request, livro):
    origem = request.get_full_path()
    try:
        item = Livro.objects.get(titulo=livro)
        tipo = 'livro'
        autor = item.autor
        empresa = item.editora
        total = 0 #item.paginas

        capitulos = [item.cap_1, item.cap_2, item.cap_3, item.cap_4, item.cap_5,
                     item.cap_6, item.cap_7, item.cap_8, item.cap_9, item.cap_10,
                     item.cap_11, item.cap_12, item.cap_13, item.cap_14, item.cap_15]

        for i in capitulos:
            if i.__len__() is not 0:
                total = total + 1
    except Livro.DoesNotExist:
        erro = 'Livro não encontrado'
        raise Http404('Erro: {}. Origem: {}'.format(erro, origem),{
            'erro': erro,
            'origem': origem,
        })

    return render(request, 'Loja/livro.html', {
        'item': item,
        'capa': item.capa.url,
        'autor': autor,
        'tamanho': item.ficheiro.size,
        'empresa': empresa,
        'titulo': item.titulo,
        'capitulos': capitulos,
        'paginas': item.paginas,
        'total': total,
        'pagina': 'Livro',
        'main': 'loja',
    })



##################################################################

