from django.test import TestCase
from django.urls import reverse
from datetime import date
from piloto.models import Aluno, Situacao, Curso, FormaIngresso, Campus
from piloto.forms.AlunoForm import AlunoForm
from rest_framework.test import APIClient
from rest_framework import status

class AlunoModelTest(TestCase):
    def setUp(self):
        self.campus = Campus.objects.create(nome="Campus Teste")
        self.curso = Curso.objects.create(nome="Engenharia", campus=self.campus)
        self.situacao = Situacao.objects.create(nome="Ativo", estaNaInstituicao=True)
        self.forma_ingresso = FormaIngresso.objects.create(nome="Vestibular")

    def test_cria_aluno_e_matricula(self):
        aluno = Aluno.objects.create(
            nomeCompleto="João Silva",
            cpf="12345678901",
            curso=self.curso,
            formaIngresso=self.forma_ingresso
        )
        self.assertEqual(aluno.nomeCompleto, "João Silva")
        self.assertTrue(aluno.matricula)
        self.assertEqual(aluno.situacao, self.situacao)
        self.assertTrue(aluno.ativo)
        self.assertEqual(aluno.dataCadastro, date.today())

class AlunoFormTest(TestCase):
    def setUp(self):
        self.campus = Campus.objects.create(nome="Campus Teste")
        self.curso = Curso.objects.create(nome="Computação", campus=self.campus)
        self.forma_ingresso = FormaIngresso.objects.create(nome="ENEM")

    def test_form_valido(self):
        data = {
            'nomeCompleto': 'Ana',
            'cpf': '12345678900',
            'curso': self.curso.id,
            'formaIngresso': self.forma_ingresso.id,
            'dataNascimento': '2000-01-01'
        }
        form = AlunoForm(data=data)  # Agora é uma classe, não um módulo
        self.assertTrue(form.is_valid())

    def test_form_invalido(self):
        form = AlunoForm(data={})  # Agora é uma classe, não um módulo
        self.assertFalse(form.is_valid())
        self.assertIn('nomeCompleto', form.errors)
        self.assertIn('cpf', form.errors)
        self.assertIn('curso', form.errors)
        self.assertIn('formaIngresso', form.errors)

class AlunoAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.campus = Campus.objects.create(nome="Campus Teste")
        self.curso = Curso.objects.create(nome="Engenharia", campus=self.campus)
        self.situacao = Situacao.objects.create(nome="Ativo", estaNaInstituicao=True)
        self.forma_ingresso = FormaIngresso.objects.create(nome="Vestibular")
        self.aluno = Aluno.objects.create(
            nomeCompleto="João Silva",
            cpf="12345678901",
            curso=self.curso,
            formaIngresso=self.forma_ingresso,
            situacao=self.situacao
        )

    def test_lista_alunos(self):
        url = reverse('apiAlunos')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(resp.data), 1)

    def test_detalhe_aluno(self):
        url = reverse('deleteAluno', args=[self.aluno.id])
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual(resp.data['nomeCompleto'], "João Silva")
