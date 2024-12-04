import { Component } from '@angular/core';
import { NavController } from '@ionic/angular'; // Importando NavController
import { ApiService } from './../service/api.service';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  dados: any[] = []; // Declare como um array genérico

  constructor(
    private apiService: ApiService, 
    private navCtrl: NavController
  ) {
    this.getData();
  }

  // Método para pegar os dados da API
  getData() {
    this.apiService.getData().subscribe(
      (data: any[]) => { // Receba como array de `any`
        console.log(data);
        this.dados = data; // Armazene os dados
      },
      error => {
        console.error("Erro ao buscar dados:", error); // Tratamento de erro
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
