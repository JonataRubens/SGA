from rest_framework import generics
from piloto.models import Aluno
from piloto.serializers import AlunoSerializer

class AlunoListCreateView(generics.ListCreateAPIView):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
