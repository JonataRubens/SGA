from datetime import date
from django.db import models
from piloto.models import Situacao, FormaIngresso, Curso
SITUACOES_ATIVAS = ["Vinculado", "Trancado"]

class Aluno(models.Model):
    nomeCompleto = models.CharField('Nome completo', max_length=500, help_text='')
    cpf = models.CharField('CPF', max_length=11, unique=True, help_text='')
    matricula = models.CharField('Matricula', max_length=10, unique=True, editable=False)
    curso = models.ForeignKey(Curso, verbose_name="Curso", on_delete=models.PROTECT)
    dataNascimento = models.DateField("Data de nascimento", null=True, blank=True)
    foto = models.ImageField("Foto Aluno", upload_to='alunos_fotos/', blank=True, null=True)
    formaIngresso = models.ForeignKey(FormaIngresso, verbose_name="Forma de Ingresso", on_delete=models.PROTECT)

    situacao = models.ForeignKey(Situacao, verbose_name="Situação", on_delete=models.PROTECT, default=lambda: Situacao.objects.get(nome="Vinculado"))

    ######DADOS DE CONTROLE#######
    dataCadastro = models.DateField('data de cadastro', default=date.today)
    dataUpdate = models.DateTimeField('Ultima atualização', auto_now=True)  
    ativo = models.BooleanField("Aluno vinculado na instituição?", default=True)

    def __str__(self):
        return f"{self.nomeCompleto} ({self.matricula})"
    
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"

    def save(self, *args, **kwargs):
        if not self.pk and not self.matricula:
            self.matricula = self.gerarMatricula()

        # Atualizar o campo 'ativo' com base na situação
        if self.situacao and self.situacao.nome not in SITUACOES_ATIVAS:
            self.ativo = False
        else:
            self.ativo = True

    # Salvar apenas uma vez
        super().save(*args, **kwargs)
    # def GerarMatricula(self):
    #     ano = self.dataCadastro.strftime('%Y') 
    #     semestre = '1' if self.dataCadastro.month <= 6 else '2'
    #     ultima_matricula = Aluno.objects.filter(matricula__startswith=f'{ano}{semestre}').order_by('-matricula').first()
    #     sequencia = int(ultima_matricula.matricula[-4:]) + 1 if ultima_matricula else 1
    #     return f'{ano}{semestre}{str(sequencia).zfill(4)}'

    def gerarMatricula(self):
        from django.db.models import Max

        # Obter o ano e o semestre com base na data de cadastro
        ano = self.dataCadastro.strftime('%Y') 
        semestre = '1' if self.dataCadastro.month <= 6 else '2'

        # Filtrar o maior número de sequência para o ano/semestre
        prefixo = f'{ano}{semestre}'
        ultima_matricula = Aluno.objects.filter(matricula__startswith=prefixo).aggregate(Max('matricula'))

        # Extrair a maior sequência ou começar com 1
        if ultima_matricula['matricula__max']:
            maior_sequencia = int(ultima_matricula['matricula__max'][-4:])
            sequencia = maior_sequencia + 1
        else:
            sequencia = 1

        # Retornar a matrícula completa
        return f'{prefixo}{str(sequencia).zfill(4)}'

