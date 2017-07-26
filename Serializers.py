"""
Serializers.py
Written by Leo Neto
Updated on July 26, 2017

"""

from rest_framework import serializers
from Blog.models import *
from Ek.models import *
from Loja.models import *
from Portfolio.models import *

class PessoaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pessoa
        fields = ('id','nome','tutor','autor','bio')
#end PessoaSerializers

class ArtigoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artigo
        fields = ('titulo', 'autor', 'sumario', 'artigo', 'tema', 'data')
#end ArtigoSerializers

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projecto
        fields = ('nome', 'autor', 'informacao', 'capa', 'data')

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ('titulo', 'artista', 'gravadora', 'capa')