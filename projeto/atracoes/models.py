from django.db import models

# Create your models here.


class Atracao(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    horario_funcionamento = models.CharField(max_length=50)
    idade_minima = models.IntegerField()


    def __str__(self):
        return self.nome