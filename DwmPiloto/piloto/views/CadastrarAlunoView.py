from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from piloto.forms.AlunoForm import AlunoForm
from piloto.models import Aluno

class CadastrarAlunoView(CreateView):
    model = Aluno
    form_class = AlunoForm
    template_name = 'edit_Aluno/NewAluno.html'
    success_url = reverse_lazy('cadastrarAluno')