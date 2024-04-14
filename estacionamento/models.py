from django.db import models

class Dono(models.Model):
    nome = models.CharField(max_length=150)
    telefone = models.CharField(max_length=12)
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.nome

class Veiculo(models.Model):
    placa = models.CharField(max_length=10)
    modelo = models.CharField(max_length=100, default = 'Desconhecido')
    marca = models.CharField(max_length=100, default = 'Desconhecido')
    proprietario = models.ForeignKey(Dono, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.placa})"

class Patio(models.Model):
    numeroVaga = models.CharField(max_length=10, unique=True)
    ocupada = models.BooleanField(default=False)
    veiculo = models.OneToOneField(Veiculo, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.numero_vaga

class Pagamento(models.Model):
    responsavel = models.ForeignKey(Dono, on_delete=models.CASCADE, default='')
    valor = models.DecimalField(max_digits=10, decimal_places = 2)
    Pagamento = models.BooleanField(default=False)