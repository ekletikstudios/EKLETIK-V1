# This Python file uses the following encoding: utf-8
from ModelsLibraries import *
from Choices import *


######################### ---------------------------------------
class Album(models.Model):
    tipo = 'Álbum'
    safeTipo = 'album'
    titulo = models.CharField(max_length=100)
    artista = models.CharField(max_length=50)
    gravadora = models.CharField(max_length=50)
    capa = models.ImageField(upload_to='Loja/Albums', max_length=100, default=0)
    editorial = models.CharField(max_length=500, blank=True)
    ficheiro = models.FileField(upload_to='Vendas', max_length=100, default=0, verbose_name='Ficheiro a baixar')
    preco = models.FloatField(default=0, verbose_name='Preço em dólares')
    download = models.BooleanField(default=True, verbose_name='Pra baixar')
    status = models.CharField(choices=STATUS_CHOICES, max_length=1, default='d')

    def __str__(self):
        return self.titulo
#end Album


class Faixa(models.Model):
    numero = models.IntegerField(default=0)
    titulo = models.CharField(max_length=100)
    preco = models.FloatField(default=0, verbose_name='Preço')
    ficheiro = models.FileField(upload_to='Music', max_length=100, blank=True)
    album = models.ForeignKey(Album, default=1)
    def __str__(self):
        return self.titulo
#end Faixas










########## -----------------------------------------------

class Capitulos(models.Model):
    titulo = models.CharField(max_length=100)
    def __str__(self):
        return self.titulo
#end Capitulos



class Livro(models.Model):
    tipo = 'Livro'
    safeTipo = 'livro'
    titulo = models.CharField(max_length=50)
    autor = models.CharField(max_length=50)
    lancamento = models.DateField(auto_now=False, default=date.today, verbose_name='Lançamento')
    editora = models.CharField(max_length=50)
    paginas = models.IntegerField(verbose_name='Páginas')
    capa = models.ImageField(upload_to='Loja/Livros', max_length=100, default=0)

    cap_1 = models.CharField(max_length=70, blank=True)
    cap_2 = models.CharField(max_length=70, blank=True)
    cap_3 = models.CharField(max_length=70, blank=True)
    cap_4 = models.CharField(max_length=70, blank=True)
    cap_5 = models.CharField(max_length=70, blank=True)
    cap_6 = models.CharField(max_length=70, blank=True)
    cap_7 = models.CharField(max_length=70, blank=True)
    cap_8 = models.CharField(max_length=70, blank=True)
    cap_9 = models.CharField(max_length=70, blank=True)
    cap_10 = models.CharField(max_length=70, blank=True)
    cap_11 = models.CharField(max_length=70, blank=True)
    cap_12 = models.CharField(max_length=70, blank=True)
    cap_13 = models.CharField(max_length=70, blank=True)
    cap_14 = models.CharField(max_length=70, blank=True)
    cap_15 = models.CharField(max_length=70, blank=True)
    editorial = models.CharField(max_length=500, blank=True)
    ficheiro = models.FileField(upload_to='Vendas', max_length=100, default=0, verbose_name='Ficheiro a baixar')
    preco = models.FloatField(default=0, verbose_name='Preço em dólares')
    download = models.BooleanField(default=True, verbose_name='Pra baixar')
    status = models.CharField(default='r', choices=STATUS_CHOICES, max_length=1)
    def __str__(self):
        return self.titulo
#end Livro
