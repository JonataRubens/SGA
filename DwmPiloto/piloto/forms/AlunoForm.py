from django import forms
from piloto.models import Aluno


class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nomeCompleto', 'cpf', 'curso', 'situacao',
            'dataNascimento', 'foto', 'formaIngresso'
        ]