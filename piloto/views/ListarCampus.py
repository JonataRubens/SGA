from django.views.generic import TemplateView
from piloto.models import Campus

class ListarCampus(TemplateView):
    template_name = 'listas/ListarCampus.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Obter todos os campi com seus cursos relacionados
        campi = Campus.objects.prefetch_related('curso_set').all()

        # Adicionar os campi ao contexto
        context['campi'] = campi
        return context
