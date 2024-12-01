import { ApiService } from './../service/api.service';
import { Component } from '@angular/core';
import { AlertController, NavController } from '@ionic/angular';

@Component({
  selector: 'app-home',
  templateUrl: 'home.page.html',
  styleUrls: ['home.page.scss'],
})
export class HomePage {
  dados: any[] = []; // Lista de alunos

  constructor(
    private apiService: ApiService,
    private alertController: AlertController, // Adicionado para usar o ion-alert
    private navCtrl: NavController
  ) {
    this.getData();
  }

  // Busca os dados da API
  getData() {
    this.apiService.getData().subscribe(
      (data: any[]) => {
        console.log(data);
        this.dados = data;
      },
      error => {
        console.error('Erro ao buscar dados:', error);
      }
    );
  }

  // Mostra uma confirmação antes de deletar
  async confirmarDelecao(id: number) {
    const alert = await this.alertController.create({
      header: 'Confirmar Exclusão',
      message: 'Tem certeza que deseja excluir este aluno?',
      buttons: [
        {
          text: 'Cancelar',
          role: 'cancel',
          handler: () => {
            console.log('Exclusão cancelada');
          },
        },
        {
          text: 'Excluir',
          handler: () => {
            this.deletarAluno(id); // Chama o método para excluir
          },
        },
      ],
    });

    await alert.present();
  }

  // Deleta um aluno pelo ID
  deletarAluno(id: number) {
    this.apiService.deleteAluno(id).subscribe(
      () => {
        console.log(`Aluno com ID ${id} deletado com sucesso.`);
        // Atualiza a lista após deletar
        this.dados = this.dados.filter(aluno => aluno.id !== id);
      },
      error => {
        console.error('Erro ao deletar aluno:', error);
      }
    );
  }

  // Volta para a página anterior
  goBack() {
    this.navCtrl.back();
  }
}
