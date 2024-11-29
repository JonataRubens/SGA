from rest_framework import serializers
from piloto.models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'nomeCompleto', 'cpf', 'curso', 'situacao',
            'dataNascimento', 'foto', 'formaIngresso'
        ]