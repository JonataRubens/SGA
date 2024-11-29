from django.db import models

class Situacao(models.Model):
    nome = models.CharField("Nome Da Situacao", max_length=50)

    class Meta:
        verbose_name = "Situação"
        verbose_name_plural = "Situações"

    def __str__(self):
        return self.nome
