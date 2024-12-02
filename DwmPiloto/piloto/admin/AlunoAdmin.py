from django.contrib import admin
from piloto.models import Aluno, Situacao

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto', 'cpf', 'matricula', 'curso', 'getCampus', 'situacao', 'formaIngresso', 'dataCadastro', 'estaNaInstituicao', 'ativo')
    search_fields = ('nomeCompleto', 'cpf', 'matricula')
    #list_filter = ('curso', 'formaIngresso', 'ativo')
    readonly_fields = ()
    exclude = ('dataCadastro', 'matricula',) 

    def getCampus(self, obj):
        return obj.curso.campus.nome  
    getCampus.short_description = 'Campus'

    def estaNaInstituicao(self, obj):
        # Acessando a situação do aluno e retornando o valor de "estaNaInstituicao"
        situacao = Situacao.objects.filter(aluno=obj).first()  # Ajuste conforme seu modelo de relacionamento
        return situacao.estaNaInstituicao if situacao else False
    estaNaInstituicao.short_description = "ativo na instituicao"
    estaNaInstituicao.boolean = True

    def situacao(self, obj):
        return obj.situacao.nome  # Aqui acessamos o nome da situação, ajuste conforme o campo do modelo Situacao
    situacao.short_description = 'Situação'
