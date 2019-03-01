from django.db import models
from django.utils.text import slugify

from catalogo.managers import ProdutoManager


class Categoria(models.Model):
    nome = models.CharField(max_length=30)
    slug = models.SlugField(max_length=30)

    def __str__(self):
        return self.nome

    def produtos(self):
        return self.produto_set.all()


class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    objects = ProdutoManager()

    def __str__(self):
        return self.nome

    def as_dict(self):
        return {
            "categoria": self.categoria.nome,
            "nome": self.nome
        }

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.nome)
        return super().save(*args, **kwargs)
