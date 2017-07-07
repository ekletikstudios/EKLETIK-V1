# -*- coding: utf-8 -*-

# Django Essentials
from __future__ import unicode_literals
from django.contrib import admin
#from markdownx.admin import MarkdownxModelAdmin
#from markdownx.widgets import AdminMarkdownxWidget

# Importing Project Models
from Ek.models import *
from Loja.models import *
from Blog.models import *
from Azinca.models import *
from Portfolio.models import *
from Receitas.models import *
from Pesquisar.models import *
from Forum.models import *




# Actions for the Admin Panel...
def make_published(modeladmin, request, queryset):
    queryset.update(status='p')
make_published.short_description = "Publicar elementos selecionados"

def make_draft(modeladmin, request, queryset):
    queryset.update(status='d')
make_draft.short_description = "Ocultar elementos selecionados"

def make_destaque(modeladmin, request, queryset):
    queryset.update(destaque=True)
make_destaque.short_description = "Destacar elementos selecionados"

def make_NoDestaque(modeladmin, request, queryset):
    queryset.update(destaque=False)
make_NoDestaque.short_description = "Não destacar os elementos selecionados"

#################################################################








# Admin Inlines (Models that include others)...
class FaixasInLine(admin.TabularInline):
    model = Faixa

class LivroInLine(admin.TabularInline):
    model = Livro

#class TextoInLine(admin.StackedInline):
#    model = Texto

class ArtigoInLine(admin.StackedInline):
    model = Artigo
#################################################################





# Main models in the admin panel...
class ArtigoAdmin(admin.ModelAdmin):
    #inlines = [TextoInLine]
    ordering = ['-data']
    list_display  = ['titulo', 'autor', 'destaque', 'tema', 'richmedia', 'status', 'data']
    list_per_page = 20
    actions = [make_published, make_draft, make_destaque, make_NoDestaque]
#end ArtigosAdmin


class PessoaAdmin(admin.ModelAdmin):
    inlines = [
        ArtigoInLine
    ]
    ordering = ['nome']
    list_display = ['nome', 'departamentos', 'tutor', 'autor']
    list_per_page = 20
    actions = [make_published, make_draft]
    short_description = 'nome'
#end PessoaAdmin


class ProjectoAdmin(admin.ModelAdmin):
    ordering = ['-data']
    list_display = ['nome', 'destaque', 'status', 'autor', 'cliente','tipo', 'data']
    actions = [make_draft, make_published]
#end ProjectoAdmin


class SolicitacaoAdmin(admin.ModelAdmin):
    ordering = ['nomeDoCliente']
    list_display = ['nomeDoCliente']
#end SolicitacaoAdmin



class AlbumAdmin(admin.ModelAdmin):
    inlines = [
        FaixasInLine
    ]
    ordering = ['titulo']
    list_display = ['titulo', 'artista', 'gravadora', 'status', 'download']
    actions = [make_draft, make_published]


class LivroAdmin(admin.ModelAdmin):
    ordering = ['titulo']
    list_display = ['titulo', 'autor', 'editora', 'lancamento', 'preco', 'download']

#################################################################











# Registering Models to the Admin Panel
admin.site.register(Artigo, ArtigoAdmin)
admin.site.register(Projecto, ProjectoAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Livro, LivroAdmin)
# admin.site.register(Texto, MarkdownxModelAdmin)
#admin.site.register(Item, ItemAdmin)
#admin.site.register(Solicitacao, SolicitacaoAdmin)
#admin.site.register(Pessoa, PessoaAdmin)