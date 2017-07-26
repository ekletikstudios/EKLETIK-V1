"""

EKLETIK URL Configuration
Written by Leo Neto
Updated on July 26, 2017

"""

# Importing Django stuff...
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls import include
from django.conf.urls.static import static

# Importing Model Views
from Ek import views as EK
from Azinca import views as A
from Blog import views as B
from Forum import views as F
from Portfolio import views as P
from Loja import views as L
from Receitas import views as R
from Pesquisar import views as Pesquisar

# Importing REST API
from rest_framework.urlpatterns import format_suffix_patterns

# URL Patterns
urlpatterns = [
    # Admin / Auth / Status Codes
    url(r'^404', EK.error_404, name='404'),
    url(r'^admin.*', EK.Erro, name='404'),
    url(r'^dash.*', EK.Erro, name='404'),
    url(r'^wp.*', EK.Erro, name='404'),
    url(r'^login.*', EK.Erro, name='404'),
    url(r'^door/', admin.site.urls),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),

    # Main site URLs
    url(r'^$', EK.home, name='home'),
    url(r'^empresa/', EK.empresa, name='empresa'),
    url(r'^portfolio/(?P<item>\D+)', P.portfolioItem, name='portfolioItem'),
    url(r'^portfolio/', P.portfolio, name='portfolio'),
    url(r'^contacto/', EK.contacto, name='contacto'),
    url(r'^pedido/', EK.pedido, name='pedido'),

    # Blog URLs
    url(r'^django/', B.django, name='Django'),
    url(r'^blog/django/', B.django, name='Django'),
    url(r'^blog/adicionar$', B.artigo_add, name='addArtigo'),
    url(r'^blog/add$', B.artigo_add, name='addArtigo'),
    url(r'^blog/autor/(?P<autor>\D+)', B.doautor, name='doautor'),
    url(r'^blog/(?P<titulo>\D+)', B.artigo, name='artigo'),
    url(r'^blog/', B.blog, name='blog'),

    # Loja URLs
    url(r'^loja/(?P<album>\D+)', L.LojaAlbum, name='album'),
    url(r'^loja/(?P<livro>\D+)', L.LojaLivro, name='livro'),
    url(r'^loja/compra/(?P<keyword>\D+)/', L.Compra, name='Compra'),
    url(r'^loja/', L.Loja, name='loja'),

    # Pesquisar
    url(r'^procurar/resultados/', Pesquisar.Results, name='Results'),
    url(r'^procurar/', Pesquisar.Pesquisar, name='Pesquisar'),
    url(r'^pesquisar/resultados/', Pesquisar.Results, name='Results'),
    url(r'^pesquisar/', Pesquisar.Pesquisar, name='Pesquisar'),

    # Developer APIs
    url(r'^api/albums', L.AlbumListAPI.as_view()),
    url(r'^api/articles', B.ArtigoListAPI.as_view()),
    url(r'^api/pessoas', EK.PessoaListAPI.as_view()),
    url(r'^api/portfolio', P.PortfolioListAPI.as_view()),
    url(r'^apis/', EK.Brevemente, name='apis'),
    url(r'^api/', EK.Brevemente, name='api'),

    # Coming Soon...
    url(r'^azinca/', EK.Brevemente, name='azinca'),
    url(r'^receitas/', EK.Brevemente, name='receitas'),
    url(r'^vimos/', EK.Brevemente, name='vimos'),
    url(r'^designers/', EK.Brevemente, name='designers'),
    url(r'^developers/', EK.Brevemente, name='developers'),
    url(r'^forum/', EK.Brevemente, name='forum'),
    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemap}, name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# REST API URL Configuration...
urlpatterns = format_suffix_patterns(urlpatterns)