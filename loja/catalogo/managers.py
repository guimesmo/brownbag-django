from django.db import models


class ProdutoManager(models.Manager):
    def for_categoria(self, categoria):
        return self.filter(categoria=categoria)
