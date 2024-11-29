from django import forms
from piloto.models import Situacao


class IngressoForm(forms.ModelForm):
    class Meta:
        model = Situacao
        fields = ['nome']