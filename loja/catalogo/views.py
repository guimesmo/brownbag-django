from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404, ListAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework.test import APILiveServerTestCase
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from catalogo.serializers import ProdutoSerializer
from .models import Produto
import json


class ProductListView(ListAPIView):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()


class ProductCreateView(CreateAPIView):
    serializer_class = ProdutoSerializer


class ProdutoViewSet(ModelViewSet):
    serializer_class = ProdutoSerializer
    queryset = Produto.objects.all()



class ProductView(APIView):
    """Alguma documentação para a API"""
    def get(self, request, slug=None):
        if slug:
            produto = get_object_or_404(Produto, slug=slug)
            return Response(ProdutoSerializer(produto).data)
        return Response('')

    def post(self, request):
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            produto = serializer.save()
            return Response(produto.as_dict())
        else:
            return Response("Invalido")

    def patch(self, request, slug):
        produto = Produto.objects.get(slug=slug)
        for key, val in request.data.items():
            setattr(produto, key, val)
        produto.save()
        return Response(produto.as_dict())


@api_view(['GET', 'POST', 'PATCH', 'DELETE'])
def view_produto(request, slug):
    produto = Produto.objects.get(slug=slug)
    if request.method == 'POST':
        produto.nome = request.data.get('nome')
        produto.save()
    if request.method == 'PATCH':
        for key, val in request.data.items():
            setattr(produto, key, val)
        produto.save()
    if request.method == 'DELETE':
        produto.delete()
        return Response('excluido')
    return Response(produto.as_dict())

def view_produto_old(request, slug):
    produto = Produto.objects.get(slug=slug)
    return HttpResponse(json.dumps(produto.as_dict(), ensure_ascii=False), content_type="application/json")
