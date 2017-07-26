from ViewsLibraries import *
from Ek.models import *

# Receitas Views
def receitas(request):
    #a = HttpRequest()
    return render(request, 'Receitas/receitas.html',{
        'main': 'home',
        'pagina': 'Receitas',
        #'id': a,
    })


#####################################################

