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
    tipo = p.tipo
    Cores = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0

    #tipo = p.get_tipo_display()
    if p.cor_1:
        Cores = Cores + 1
        c1 = p.cor_1
    if p.cor_2:
        Cores = Cores + 1
        c2 = p.cor_2
    if p.cor_3:
        Cores = Cores + 1
        c3 = p.cor_3
    if p.cor_4:
        Cores = Cores + 1
        c4 = p.cor_4

    return render(request, 'Ek/portfolio-item.html',{
        'main': 'portfolio',
        'pagina': 'Portfolio',
        'item': p,
        'tipo': tipo,
        'descricao': p.informacao,
        'autor': p.autor,
        'nome': p.nome,
        'capa': p.capa.url,
        'cliente': p.cliente,
        'cores': Cores,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'paleta': [c1, c2, c3, c4],
        'software': p.detalhes_tecnicos,
    })

def portfolioAdd(request):
    a = 1
