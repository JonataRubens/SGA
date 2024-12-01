from django import forms

from piloto.models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'campus']