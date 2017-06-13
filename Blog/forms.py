from django import forms
from Blog.models import *

class ArtigoForm(forms.ModelForm):
    class Meta:
        model = Artigo
        fields=('titulo','autor', 'richmedia', 'destaque', 'artigo')