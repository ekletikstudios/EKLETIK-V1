"""
Serializers.py
Written by Leo Neto
Updated on July 26, 2017

"""

from rest_framework.serializers import ModelSerializer
from Blog.models import *
from Ek.models import *
from Loja.models import *
from Portfolio.models import *

class PessoaSerializer(ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','nome','tutor','autor','bio')
#end PessoaSerializers

class ArtigoSerializer(ModelSerializer):
    class Meta:
        model = Artigo
        fields = ('id', 'titulo', 'autor', 'sumario', 'artigo', 'tema', 'data')
#end ArtigoSerializers

class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Projecto
        fields = ('id', 'nome', 'autor', 'informacao', 'capa', 'data')

class AlbumSerializer(ModelSerializer):
    class Meta:
        model = Album
        fields = ('id', 'titulo', 'artista', 'gravadora', 'capa')