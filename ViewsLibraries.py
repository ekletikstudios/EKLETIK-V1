# This Python file uses the following encoding: utf-8
from __future__ import unicode_literals
from django.http import HttpRequest, Http404, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, logout, login


PAGINAS = ['azinca', 'blog', 'Ek', 'Ekletik', 'Forum', 'Loja', 'Store', 'Pesquisar', 'Search', 'Portfolio', 'Receitas', 'Recipes']
TIPOS = ['artigos', 'blog', 'posts', 'usuarios', 'users']