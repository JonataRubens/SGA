from rest_framework import generics
from piloto.models import Aluno
from piloto.serializers import AlunoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from piloto.models import Campus, Curso

class AlunoListView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class AlunoDeleteView(APIView):
    def get(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            serializer = AlunoSerializer(aluno)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado!"}, status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk, *args, **kwargs):
        try:
            aluno = Aluno.objects.get(pk=pk)
            aluno.delete()
            return Response({"message": "Aluno deletado com sucesso!"}, status=status.HTTP_204_NO_CONTENT)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado!"}, status=status.HTTP_404_NOT_FOUND)
        
class CampusCursosListView(APIView):
    def get(self, request, *args, **kwargs):
        # Obter todos os campi e seus cursos associados
        campus_list = Campus.objects.all()

        # Preparar os dados de resposta
        data = []
        for campus in campus_list:
            cursos = campus.curso_set.all()  # Obtém todos os cursos relacionados ao campus
            campus_data = {
                'id': campus.id,
                'nome': campus.nome,  # Supondo que o campo do nome do campus seja 'nome'
                'cursos': [{'id': curso.id, 'nome': curso.nome} for curso in cursos]  # Supondo que o campo do nome do curso seja 'nome'
            }
            data.append(campus_data)

        return Response(data, status=status.HTTP_200_OK)
    