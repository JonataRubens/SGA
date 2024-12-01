from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from piloto.models import Campus
from piloto.serializers import CampusSerializer

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
