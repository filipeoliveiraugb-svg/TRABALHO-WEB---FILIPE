from rest_framework import serializers
from.models import Cliente,Venda,Estoque,Medicamento

class MedicamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicamento
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    medicamento = serializers.StringRelatedField()
    cliente = serializers.StringRelatedField()

    class Meta:
        model = Venda
        fields = '__all__'

class EstoqueSerializer(serializers.ModelSerializer):
    medicamento = serializers.StringRelatedField()

    class Meta:
        model = Estoque
        fields = '__all__'
