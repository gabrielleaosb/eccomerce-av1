from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    lancamento = models.DateField(null=True, blank=True)
    desenvolvedor = models.CharField(max_length=155, null=True, blank=True)
    distribuidor = models.CharField(max_length=155, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name='produtos', null=True)

    def __str__(self):
        return self.nome