from django import forms
from piloto.models import Campus


class CampusForm(forms.ModelForm):
    class Meta:
        model = Campus
        fields = ['nome']

        widgets = {
            'nome': forms.TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Digite o nome do campus'
            }),
        }