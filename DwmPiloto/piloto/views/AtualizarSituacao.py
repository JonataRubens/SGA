from django.shortcuts import get_object_or_404, redirect
from django.views.generic import View
from piloto.models import Aluno, Situacao

class AtualizarSituacaoView(View):
    def post(self, request, pk):
        aluno = get_object_or_404(Aluno, pk=pk)
        situacao_id = request.POST.get('situacao')
        situacao = Situacao.objects.get(id=situacao_id)
        aluno.situacao = situacao
        aluno.save()
        return redirect('listaAlunos')  # Redireciona de volta para a lista de alunos
