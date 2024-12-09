from django import forms

from piloto.models import Curso


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nome', 'campus']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Digite o nome do curso'
            }),
            'campus': forms.Select(attrs={
                'class': 'form-control',
                'placeholder': 'Selecione o campus'
            }),
        }