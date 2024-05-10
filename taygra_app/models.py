from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=100)
    imagem_url = models.CharField(max_length=100, blank=True, null=True)
    preco = models.DecimalField(decimal_places=2)
    desconto = models.DecimalField(decimal_places=2, max_digits=5, default=0) # falta verificar negativo
    descricao = models.CharField(max_length=255)
    detalhes = models.TextField()
    quantidade_vendida = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    quantidade_estoque = models.IntegerField(validators=[MinValueValidator(0)], default=0)
    fk_categoria = models.ForeignKey("Categoria", on_delete=models.PROTECT, blank=True, null=True)
    fk_cor = models.ForeignKey("Cor", on_delete=models.CASCADE, blank=True, null=True)
    fk_tamanho = models.ForeignKey("Tamanho", on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Tamanho(models.Model):
    valor = models.CharField(max_length=100)

    def __str__(self):
        return self.valor
    
class Cor(models.Model):
    nome = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nome
    
class Comentario(models.Model):
    autor = models.CharField(max_length=100)
    descricao = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    avaliacao = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    fk_produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.autor + " - " + self.avaliacao + "/5"
    
class Oferta(models.Model):
    nome = models.CharField(max_length=100)
    produtos = models.ManyToManyField("Produto")
    
    def __str__(self):
        return self.nome
    
class Usuario(User):
    nome = models.CharField(max_length=100)
    is_inscrito = models.BooleanField(default=False)
    desejos = models.ManyToManyField("Produto")
    
    def __str__(self):
        return self.nome
    
    def save(self, *args, **kwargs):
        self.nome = self.first_name + " " + self.last_name
        return super().save(*args, **kwargs)
    
class CarrinhoUsuario(models.Model):
    fk_usuario = models.ForeignKey("Usuario", on_delete=models.CASCADE)
    fk_produto = models.ForeignKey("Produto", on_delete=models.CASCADE)
    quantidade = models.IntegerField(validators=[MinValueValidator(1)], default=0)
    
    def __str__(self):
        return self.fk_usuario.nome + " - " + self.fk_produto.nome + " - " + self.quantidade
    
    
    
