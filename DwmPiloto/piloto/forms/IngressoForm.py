from django import forms

from piloto.models import FormaIngresso


class IngressoForm(forms.ModelForm):
    class Meta:
        model = FormaIngresso
        fields = ['nome']