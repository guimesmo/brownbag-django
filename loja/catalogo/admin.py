from django.contrib import admin

from .models import Produto, Categoria

admin.site.register([Produto, Categoria])