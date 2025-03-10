from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Plataforma(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Sistema(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tipo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
    
class Distribuidor(models.Model):
    nome = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    descricao = models.TextField()
    lancamento = models.DateField(null=True, blank=True)
    desenvolvedor = models.CharField(max_length=155, null=True, blank=True)
    distribuidor =  models.ForeignKey(Distribuidor, on_delete=models.SET_NULL, null=True, blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='produtos/', null=True, blank=True)
    categoria = models.ManyToManyField(Categoria, related_name='produtos')
    plataforma = models.ManyToManyField(Plataforma, related_name='produtos')
    sistema = models.ManyToManyField(Sistema, related_name='produtos')
    tipo = models.ManyToManyField(Tipo, related_name='produtos')

    def __str__(self):
        return self.nome