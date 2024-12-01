from django.urls import path
from piloto.views import CadastrarAlunoView, CampusCreateView, CursoCreateView, DefaultView, ExcluirAlunoView, ListaAlunosView, EditarAlunoView, ListarCampus, AlunoListView, LoginView, CampusCursosListView, AlunoDeleteView


urlpatterns = [
    path('', DefaultView.as_view(), name='Index'),
    path('cadastrar/', CadastrarAlunoView.as_view(), name='cadastrarAluno'),
    path('alunos/', ListaAlunosView.as_view(), name='listaAlunos'),
    path('add/curso/', CursoCreateView.as_view(), name='cadastrarCurso'),
    path('add/campus/', CampusCreateView.as_view(), name='cadastrarCampus'),
    path('editarAluno/<int:pk>/', EditarAlunoView.as_view(), name='editarAluno'),
    path('listarCampus/', ListarCampus.as_view(), name='listarCampus'),
    path('excluirAluno/<int:pk>/', ExcluirAlunoView.as_view(), name='excluirAluno'),
    path('login/', LoginView.as_view(), name='Login'),

    path('api/alunos/', AlunoListView.as_view(), name='apiAlunos'),
    path('api/campus-cursos/', CampusCursosListView.as_view(), name='campusCursos'),
    path('api/alunos/<int:pk>/', AlunoDeleteView.as_view(), name='deleteAluno'),

]