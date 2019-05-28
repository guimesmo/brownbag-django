from decimal import Decimal

from rest_framework import serializers
from .models import Produto

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        exclude = []
        model = Produto

    def validate(self, validated_data):
        if 'l' in validated_data.get('nome', '').lower():
            if validated_data.get('preco') > 20:
                raise serializers.ValidationError({"preco": "Esse preço é inválido"})
        return validated_data

    def validate_preco(self, value):
        preco = value
        if preco < 0:
            raise serializers.ValidationError("Esse preço é inválido")
        return Decimal('5')
