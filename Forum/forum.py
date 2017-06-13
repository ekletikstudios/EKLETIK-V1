# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *



# Forum Views
def forum(request):
    return render(request, 'Forum/forum.html',{
        'main': 'home',
        'pagina': 'Fórum',
    })


#####################################################


