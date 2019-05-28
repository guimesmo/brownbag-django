from django import forms

from .models import Produto


class ProdutoForm(forms.ModelForm):

    def clean_preco(self):
        preco = self.cleaned_data.get('preco')
        if preco < 0:
            raise forms.ValidationError("Esse preço é inválido")
        return preco

    class Meta:
        exclude = []
        model = Produto
