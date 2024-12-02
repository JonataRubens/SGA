from django import forms
from piloto.models import Aluno

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = [
            'nomeCompleto', 'cpf', 'curso',
            'dataNascimento', 'foto', 'formaIngresso'
        ]
        widgets = {
            'nomeCompleto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o nome completo'}),
            'cpf': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Digite o CPF'}),
            'curso': forms.Select(attrs={'class': 'form-control'}),
            'dataNascimento': forms.DateInput(attrs={
                'class': 'form-control', 'type': 'date', 'placeholder': 'Selecione a data de nascimento'
            }),
            'foto': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
            'formaIngresso': forms.Select(attrs={'class': 'form-control'}),
        }
