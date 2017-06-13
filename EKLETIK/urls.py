"""EKLETIK URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from Ek import views as EK
from Azinca import azinca as A
from Blog import blog as B
from Forum import forum as F
from Portfolio import portfolio as P
from Loja import loja as L
from Receitas import receitas as R
from Pesquisar import views as Pesquisar



from django.contrib.auth.views import *
from django.conf import settings
from django.conf.urls.static import static
#admin.autodiscover()


urlpatterns = [
    url(r'^404', EK.error_404, name='404'),
    url(r'^admin.*', EK.Erro, name='404'),
    url(r'^dash.*', EK.Erro, name='404'),
    url(r'^wp.*', EK.Erro, name='404'),
    url(r'^login.*', EK.Erro, name='404'),
    url(r'^door/', admin.site.urls),
    url(r'^logout/$', logout, {'template_name': 'admin/logout.html'}, name='logout'),

    # EK URLs
    url(r'^$', EK.home, name='home'),
    url(r'^empresa/', EK.empresa, name='empresa'),
    url(r'portfolio/(?P<item>\D+)', P.portfolioItem, name='portfolioItem'),
    url(r'^portfolio/', P.portfolio, name='portfolio'),
    url(r'^contacto/', EK.contacto, name='contacto'),
    url(r'^pedido/', EK.pedido, name='pedido'),




    # Blogue
    url(r'^blog/artigos/adicionar$', B.artigo_add, name='addArtigo'),
    url(r'^blog/add/', B.artigo_add, name='addArtigo'),
    url(r'^blog/artigos/autor/(?P<autor>\D+)', B.doautor, name='doautor'),
    url(r'^blog/artigos/(?P<titulo>\D+)', B.artigo, name='artigo'),
    url(r'^blog/', B.blog, name='blog'),



    # Loja
    url(r'^loja/producto/albums/(?P<album>\D+)', L.LojaAlbum, name='album'),
    url(r'^loja/producto/livros/(?P<livro>\D+)', L.LojaLivro, name='livro'),
    url(r'^loja/', L.Loja, name='loja'),



    # Azinca
    url(r'^azinca/', A.azinca, name='azinca'),




    # ReceitaME
    url(r'^receitas/', R.receitas, name='receitas'),
    # url(r'^receita-me/', EK.receitas, name='receita-me'),




    # Forum
    url(r'^forum/', F.forum, name='forum'),




    # Spotify
    url(r'procurar/resultados/', Pesquisar.Results, name='Results'),
    url(r'procurar/', Pesquisar.Pesquisar, name='Pesquisar'),
    url(r'pesquisar/resultados/', Pesquisar.Results, name='Results'),
    url(r'pesquisar/', Pesquisar.Pesquisar, name='Pesquisar'),

    #url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemap}, name='django.contrib.sitemaps.views.sitemap'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
