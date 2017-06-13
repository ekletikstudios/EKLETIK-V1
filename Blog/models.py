# This Python file uses the following encoding: utf-8
from ModelsLibraries import *
from Ek.models import *

# Create your models here.
class Artigo(models.Model):
    titulo   = models.CharField(max_length=100)
    autor  = models.ForeignKey(Pessoa, default=1)
    richmedia = models.BooleanField(default=False)
    destaque = models.BooleanField(default=False)
    artigo = models.TextField()
    sumario = models.CharField(max_length=350, blank=True)
    imagem = models.ImageField(upload_to='artigos', blank=True, max_length=100)

    tema  = models.CharField(max_length=20, choices=TOPIC_CHOICES, default='G')
    data   = models.DateField(auto_now=False, default=date.today)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='d')

    class Meta:
        verbose_name_plural = 'Artigos, Blogues e Notícias'

    def __str__(self):
        return self.titulo
#end Artigos
