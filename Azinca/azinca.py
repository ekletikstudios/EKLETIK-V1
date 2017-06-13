# This Python file uses the following encoding: utf-8
from ViewsLibraries import *
from Ek.models import *


# Azinca Views
def azinca(request):
    return render(request, 'Azinca/azinca.html',{
        'main': 'home',
        'pagina': 'Azinca',
    })


#####################################################