from django.db import models
from atracoes.models import Atracao
from comentarios.models import Comentario
from avaliacoes.models import Avaliacao
from localizacao.models import Localizacao

# Criar os modelos e em seguida devem ser registrados dentro do arquivo admin este arquivo esta dentro da aplicação
class  PontoTuristico(models.Model):
    nome = models.CharField(max_length=150)
    descricao = models.TextField()
    aprovado = models.BooleanField(default=False)
    atracoes = models.ManyToManyField(Atracao)
    Comentario = models.ManyToManyField(Comentario)
    avaliacoes = models.ManyToManyField(Avaliacao)
    # localizacao = models.ForeignKey(Localizacao, on_delete=models.CASCADE)



    def __str__(self):
        return self.nome
