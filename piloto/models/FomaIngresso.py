from django.db import models

class FormaIngresso(models.Model):
    nome = models.CharField("Forma de ingresso", max_length=50, unique=True)

    class Meta:
        verbose_name = "Ingresso"
        verbose_name_plural = "formaIngresso"

    def __str__(self):
        return self.nome
