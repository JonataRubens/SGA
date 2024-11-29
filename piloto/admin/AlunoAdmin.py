from django.contrib import admin
from piloto.models import Aluno

@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nomeCompleto', 'cpf', 'matricula', 'curso','getCampus', 'formaIngresso', 'situacao', 'dataCadastro', 'ativo')
    search_fields = ('nomeCompleto', 'cpf', 'matricula')
    list_filter = ('curso', 'situacao', 'formaIngresso', 'ativo')
    readonly_fields = ()
    exclude = ( 'ativo', 'dataCadastro', 'matricula',) 

    def getCampus(self, obj):
        return obj.curso.campus.nome  
    getCampus.short_description = 'Campus'


