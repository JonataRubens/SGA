from django.urls import reverse_lazy
from piloto.models import Aluno
from piloto.forms.AlunoForm import AlunoForm
from django.views.generic import UpdateView

class EditarAlunoView(UpdateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'edit_Aluno/EditAluno.html'
    context_object_name = 'aluno'

    # Quando o formulário for salvo, redireciona para a lista de alunos
    def get_success_url(self):
        return reverse_lazy('listaAlunos')
