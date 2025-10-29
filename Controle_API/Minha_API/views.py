from django.shortcuts import render
from rest_framework import viewsets
from .models import Medicamento, Cliente, Venda, Estoque
from .serializers import (
    MedicamentoSerializer,
    ClienteSerializer,
    VendaSerializer,
    EstoqueSerializer
)

class MedicamentoViewSet(viewsets.ModelViewSet):
    queryset = Medicamento.objects.all()
    serializer_class = MedicamentoSerializer


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer


class VendaViewSet(viewsets.ModelViewSet):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer


class EstoqueViewSet(viewsets.ModelViewSet):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer
