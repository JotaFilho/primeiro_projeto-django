from django.db import models


#Classes criadas, para criar as tabelas no SQLITE
#A Func criada com str serve para mostrar o nome do campo no lugar de object1, object2 etc...

class Produto(models.Model):
    nome = models.CharField('Nome', max_length=1000)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    estoque = models.IntegerField('Quantidade em estoque')
    
    def __str__(self):
        return self.nome

    
class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobrenome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    
    def __str__(self):
        return f'{self.nome} {self.sobrenome}'