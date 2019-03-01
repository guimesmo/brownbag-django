from django.http import HttpResponse

from .models import Produto
import json


def view_produto(request, slug):
    produto = Produto.objects.get(slug=slug)

    return HttpResponse(json.dumps(produto.as_dict(), ensure_ascii=False), content_type="application/json")
