import { Component } from '@angular/core';
import { NavController } from '@ionic/angular';
import { ApiService } from './../service/api.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  dados: any[] = []; // Declare como um array genérico
  cursos: any[] = [];  // Lista de cursos (pode vir da API ou de um serviço)
  situacoes: any[] = [];  // Lista de situações (pode vir da API ou de um serviço)
  formasIngresso: any[] = [];  // Lista de formas de ingresso (pode vir da API ou de um serviço)

  constructor(
    private apiService: ApiService, 
    private navCtrl: NavController
  ) {
    this.getData();
    this.getCursos();  // Obtém a lista de cursos
    this.getSituacoes();  // Obtém a lista de situações
    this.getFormasIngresso();  // Obtém a lista de formas de ingresso
  }

  // Método para pegar os dados da API
  getData() {
    this.apiService.getData().subscribe(
      (data: any[]) => {
        console.log(data);
        // Preenche os nomes dos cursos, situações e formas de ingresso
        this.dados = data.map((aluno: any) => {
          return {
            ...aluno,
            cursoNome: this.getCursoNome(aluno.curso),
            situacaoNome: this.getSituacaoNome(aluno.situacao),
            formaIngressoNome: this.getFormaIngressoNome(aluno.formaIngresso),
          };
        });
        console.log(this.dados);
      },
      error => {
        console.error("Erro ao buscar dados:", error);
      }
    );
  }

  // Métodos para pegar o nome do curso, situação e forma de ingresso com base no ID

  getCursoNome(cursoId: number): string {
    const curso = this.cursos.find(c => c.id === cursoId);
    return curso ? curso.nome : 'Curso não encontrado';
  }

  getSituacaoNome(situacaoId: number): string {
    const situacao = this.situacoes.find(s => s.id === situacaoId);
    return situacao ? situacao.nome : 'Situação não encontrada';
  }

  getFormaIngressoNome(formaIngressoId: number): string {
    const formaIngresso = this.formasIngresso.find(f => f.id === formaIngressoId);
    return formaIngresso ? formaIngresso.nome : 'Forma de ingresso não encontrada';
  }

  // Métodos para buscar as listas de cursos, situações e formas de ingresso

  getCursos() {
    this.apiService.getCursos().subscribe(
      (cursos: any[]) => {
        this.cursos = cursos;
      },
      error => {
        console.error("Erro ao buscar cursos:", error);
      }
    );
  }

  getSituacoes() {
    this.apiService.getSituacoes().subscribe(
      (situacoes: any[]) => {
        this.situacoes = situacoes;
      },
      error => {
        console.error("Erro ao buscar situações:", error);
      }
    );
  }

  getFormasIngresso() {
    this.apiService.getFormasIngresso().subscribe(
      (formasIngresso: any[]) => {
        this.formasIngresso = formasIngresso;
      },
      error => {
        console.error("Erro ao buscar formas de ingresso:", error);
      }
    );
  }

  // Método para navegar para a página de edição
  editarAluno(id: number) {
    this.navCtrl.navigateForward(`/editar-aluno/${id}`);
  }

  // Método para deletar aluno
  confirmarDelecao(id: number) {
    if (confirm("Tem certeza que deseja excluir este aluno?")) {
      this.apiService.deleteAluno(id).subscribe(
        () => {
          console.log("Aluno excluído com sucesso.");
          this.getData(); // Atualiza a lista de alunos
        },
        error => {
          console.error("Erro ao excluir aluno:", error);
        }
      );
    }
  }
}
