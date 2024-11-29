from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from piloto.models import Aluno

class ExcluirAlunoView(View):
    def get(self, request, pk, *args, **kwargs):
        # Recuperar o aluno pelo ID (ou retornar 404 se não existir)
        aluno = get_object_or_404(Aluno, pk=pk)
        
        # Atualizar o campo ativo para False
        Aluno.objects.filter(pk=pk).update(ativo=False)
        
        # Redirecionar para a lista de alunos
        return HttpResponseRedirect(reverse('listaAlunos'))
