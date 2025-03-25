from django.db import models

class Receita(models.Model):
    tipo = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data = models.DateField()

    def __str__(self):
        return f"{self.tipo} - {self.valor}"

class Despesa(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    data = models.DateField()
    receita = models.ForeignKey(Receita, on_delete=models.CASCADE, related_name='despesas')  # Relacionamento com Receita

    def __str__(self):
        return f"{self.nome} - {self.valor}"
