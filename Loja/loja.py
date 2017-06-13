# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from .models import *



# Loja Views...
def Loja(request):
    a = Album.objects.all().filter(status='p')#.order_by('titulo')
    l = Livro.objects.all().filter(status='p')#.order_by('titulo')
    #destaques = Item.objects.filter(destaque=True)
    return render(request, 'Loja/loja.html', {
        'main': 'home',
        'pagina': 'Loja',
        'albums': a,
        'livros': l,
        'productos': [a, l],
    })






def LojaAlbum(request, album):
    origem = request.get_full_path()
    try:
        item = Album.objects.get(titulo=album)
        faixas = Faixa.objects.filter(album=item)
        tipo = 'album'
        autor = item.artista
        empresa = item.gravadora
        total = 0 #item.faixas
        validindexes = []

        # lista = [item.faixa_1, item.faixa_2, item.faixa_3, item.faixa_4, item.faixa_5,
        #                item.faixa_6, item.faixa_7, item.faixa_8, item.faixa_9, item.faixa_10,
        #                item.faixa_11, item.faixa_12, item.faixa_13, item.faixa_14, item.faixa_15]

        lista = []

        for i in lista:
            if i.__len__() is not 0:
                total = total+1
                validindexes.append(i)

    except Album.DoesNotExist:
        erro = 'Álbum não encontrado'
        raise Http404('Erro: {}. Origem {}'.format(erro, origem),{
            'erro': erro,
            'origem': origem,
        })

    return render(request, 'Loja/producto-album.html', {
        'item': item,
        'capa': item.capa.url,
        'autor': autor,
        'tamanho': item.ficheiro.size,
        'empresa': empresa,
        'titulo': item.titulo,
        'faixas': faixas,
        'total': total,
        'pagina': 'Productos',
        'main': 'loja',
        'valid': validindexes,
    })






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
            'erro':erro,
            'origem':origem,
        })


    return render(request, 'Loja/producto-livro.html', {
        'item': item,
        'capa': item.capa.url,
        'autor': autor,
        'tamanho': item.ficheiro.size,
        'empresa': empresa,
        'titulo': item.titulo,
        'capitulos': capitulos,
        'paginas': item.paginas,
        'total': total,
        'pagina': 'Productos',
        'main': 'loja',
    })
#####################################################
