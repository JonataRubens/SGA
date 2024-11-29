from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from piloto.forms.CursoForm import CursoForm
from piloto.models import Campus, Curso

class CursoCreateView(CreateView):
    model = Curso
    form_class = CursoForm
    template_name = 'edit_Aluno/NewCurso.html'
    success_url = reverse_lazy('cadastrarCurso')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cursos'] = Curso.objects.all()  # Lista de cursos
        context['campi'] = Campus.objects.all()  # Lista de campi
        return context