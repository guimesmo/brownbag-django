from django.contrib import admin

from catalogo.forms import ProdutoForm
from .models import Produto, Categoria


class ProdutoAdmin(admin.ModelAdmin):
    form = ProdutoForm


admin.site.register(Produto, ProdutoAdmin)
admin.site.register(Categoria)
