from django.urls import reverse_lazy
from piloto.forms.CampusForm import CampusForm
from piloto.models import Campus, Curso
from django.views.generic.edit import CreateView


class CampusCreateView(CreateView):
    model = Curso
    form_class = CampusForm
    template_name = 'edit_Aluno/NewCampus.html'
    success_url = reverse_lazy('cadastrarCampus')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['campi'] = Campus.objects.all()  # Passa a lista de campi para o template
        return context