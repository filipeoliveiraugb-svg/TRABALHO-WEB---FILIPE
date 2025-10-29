from django.db import models

class Medicamento(models.Model):
    nome = models.CharField(max_length=100)
    fabricante = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=6, decimal_places=2)
    validade = models.DateField()

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField(max_length=14, unique=True)
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome


class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    medicamento = models.ForeignKey(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data_venda = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.medicamento} para {self.cliente}"


class Estoque(models.Model):
    medicamento = models.OneToOneField(Medicamento, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=0)
    ultima_atualizacao = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.medicamento} - {self.quantidade} unidades"


