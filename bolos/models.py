from django.db import models

# Create your models here.

class Bolo(models.Model):

    TIPO = [
        ("Doce", "Doce"),
        ("Apimentado", "Apimentado"),
        ("Salgado", "Salgado"),
        ("Castanha", "Castanha")
    ]    
    
    nome = models.CharField("Nome do Recheio", max_length=200)
    tipo = models.CharField("Tipo", max_length=100, choices=TIPO)
    sabor = models.ForeignKey(Item, verbose_name="Sabor",on_delete=models.CASCADE)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Bolo"
        verbose_name_plural = "Bolos" 
        


class Item(models.Model):
    sabor = models.CharField(max_length=50)
    cobertura = models.CharField(max_length=50)
    recheio = models.CharField(max_length=50)
    tamanho = models.CharField(max_length=10)
    tipodemassa = models.CharField(max_length=100)
    
    
    
    def __str__(self):
        return self.sabor
    
    class Meta:
         verbose_name = "Item"
         verbose_name_plural = "Itens"