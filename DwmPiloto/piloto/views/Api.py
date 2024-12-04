from rest_framework import generics
from piloto.models import Aluno
from piloto.serializers import AlunoSerializer, CursoSerializer, FormaIngressoSerializer, SituacaoSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from piloto.models import Campus, Curso, Situacao, FormaIngresso

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
    
class AdicionarAlunoView(generics.CreateAPIView):
    """
    API para adicionar um novo aluno.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class EditarAlunoViewAPI(generics.UpdateAPIView):
    """
    API para editar os dados de um aluno existente.
    """
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class CursoListView(APIView):
    def get(self, request):
        cursos = Curso.objects.all()
        serializer = CursoSerializer(cursos, many=True)
        return Response(serializer.data)

class SituacaoListView(APIView):
    def get(self, request):
        situacoes = Situacao.objects.all()
        serializer = SituacaoSerializer(situacoes, many=True)
        return Response(serializer.data)

class FormaIngressoListView(APIView):
    def get(self, request):
        formas_ingresso = FormaIngresso.objects.all()
        serializer = FormaIngressoSerializer(formas_ingresso, many=True)
        return Response(serializer.data)
    
class AlunoUpdateAPI(APIView):
    def patch(self, request, pk):
        try:
            aluno = Aluno.objects.get(pk=pk)
        except Aluno.DoesNotExist:
            return Response({"error": "Aluno não encontrado"}, status=status.HTTP_404_NOT_FOUND)

        serializer = AlunoSerializer(aluno, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)