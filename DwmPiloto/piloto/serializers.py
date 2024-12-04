from rest_framework import serializers
from piloto.models import Aluno, Curso, Campus, Situacao, FormaIngresso


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']  # Campos que deseja retornar para o curso

class CampusSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True)  # Relacionamento com cursos

    class Meta:
        model = Campus
        fields = ['id', 'nome', 'cursos']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nome']

class SituacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Situacao
        fields = ['id', 'nome']

class FormaIngressoSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormaIngresso
        fields = ['id', 'nome']

class AlunoSerializer(serializers.ModelSerializer):
    curso = serializers.PrimaryKeyRelatedField(queryset=Curso.objects.all())  # Aceita apenas o ID
    situacao = serializers.PrimaryKeyRelatedField(queryset=Situacao.objects.all())  # Aceita apenas o ID
    formaIngresso = serializers.PrimaryKeyRelatedField(queryset=FormaIngresso.objects.all())  # Aceita apenas o ID

    class Meta:
        model = Aluno
        fields = ['id', 'nomeCompleto', 'cpf', 'curso', 'situacao', 'formaIngresso']