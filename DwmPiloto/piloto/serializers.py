from rest_framework import serializers
from piloto.models import Aluno, Curso, Campus

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = [
            'id', 'nomeCompleto', 'cpf', 'matricula', 'curso', 
            'dataNascimento', 'foto', 'formaIngresso', 'situacao', 'ativo'
        ]
class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']  # Campos que deseja retornar para o curso

class CampusSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True)  # Relacionamento com cursos

    class Meta:
        model = Campus
        fields = ['id', 'nome', 'cursos']
