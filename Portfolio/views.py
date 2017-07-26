# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *
from .models import *

def portfolio(request):
    Projectos = Projecto.objects.filter(status='p').order_by('-data')
    return render(request, 'Ek/portfolio.html',{
        'main': 'home',
        'pagina': 'Portfolio',
        'projectos': Projectos,
        'hoje': date.today(),
    })



def portfolioItem(request, item):
    p = Projecto.objects.get(nome=item)
    cores_do_projecto = Cor.objects.filter(projecto=p)
    tipo = p.tipo

    return render(request, 'Ek/portfolio-item.html',{
        'main': 'portfolio',
        'pagina': 'Portfolio',
        'item': p,
        'tipo': tipo,
        'descricao': p.informacao,
        'autor': p.autor,
        'cores': cores_do_projecto,
        'nome': p.nome,
        'capa': p.capa.url,
        'cliente': p.cliente,
        'software': p.detalhes_tecnicos,
        'id': p.id,

    })



def portfolioNext(request, id):
    p = Projecto.objects.filter()



