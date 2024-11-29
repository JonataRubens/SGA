from django.db import models
from .Campus import Campus

class Curso(models.Model):
    nome = models.CharField("Nome do Curso", max_length=100)
    campus = models.ForeignKey(Campus, verbose_name="Campus", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"

    def __str__(self):
        return f"{self.nome} ({self.campus.nome})"