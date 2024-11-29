from django.views.generic import ListView
from piloto.models import Aluno, Campus, Curso, Situacao, FormaIngresso

class ListaAlunosView(ListView):
    model = Aluno
    template_name = 'listas/ListarAlunos.html'
    context_object_name = 'alunos'

    def get_queryset(self):
        queryset = Aluno.objects.filter(ativo=True)  # Filtra apenas os alunos ativos
        campus_filter = self.request.GET.get('campus', '')  # Captura o filtro de campus
        curso_filter = self.request.GET.get('curso', '')  # Captura o filtro de curso

        # Filtra pelo campus, se informado
        if campus_filter:
            queryset = queryset.filter(curso__campus__id=campus_filter)

        # Filtra pelo curso, se informado
        if curso_filter:
            queryset = queryset.filter(curso__id=curso_filter)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campus_options'] = Campus.objects.all()  # Envia todos os campi
        context['curso_options'] = Curso.objects.all()  # Envia todos os cursos
        context['formas_ingresso'] = FormaIngresso.objects.all()
        context['situacao_option'] = Situacao.objects.all()

        # Adiciona os filtros atuais ao contexto
        context['campus_filter'] = self.request.GET.get('campus', '')  # Último valor de campus
        context['curso_filter'] = self.request.GET.get('curso', '')  # Último valor de curso
        context['total_ativo'] = Aluno.objects.filter(ativo=True).count()
        return context