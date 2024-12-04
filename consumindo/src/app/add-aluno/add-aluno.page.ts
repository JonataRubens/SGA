import { Component } from '@angular/core';
import { ApiService } from '../service/api.service';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-add-aluno',
  templateUrl: './add-aluno.page.html',
  styleUrls: ['./add-aluno.page.scss'],
})
export class AddAlunoPage {
  aluno = {
    nomeCompleto: '',
    cpf: '',
    curso: null,
    situacao: null,
    dataNascimento: '',
    formaIngresso: null, // Atualizado para suportar o dropdown
  };

  cursos: any[] = [];
  situacoes: any[] = [];
  formasIngresso: any[] = []; // Adiciona as formas de ingresso

  constructor(private apiService: ApiService, private navCtrl: NavController) {
    this.carregarOpcoes();
  }

  // Carregar cursos, situações e formas de ingresso
  carregarOpcoes() {
    this.apiService.getCursos().subscribe(
      (data: any[]) => {
        this.cursos = data;
      },
      error => {
        console.error('Erro ao buscar cursos:', error);
      }
    );

    this.apiService.getSituacoes().subscribe(
      (data: any[]) => {
        this.situacoes = data;
      },
      error => {
        console.error('Erro ao buscar situações:', error);
      }
    );

    this.apiService.getFormasIngresso().subscribe(
      (data: any[]) => {
        this.formasIngresso = data;
      },
      error => {
        console.error('Erro ao buscar formas de ingresso:', error);
      }
    );
  }

  adicionarAluno() {
    this.apiService.addAluno(this.aluno).subscribe(
      response => {
        console.log('Aluno adicionado com sucesso!', response);
        this.navCtrl.back();
      },
      error => {
        console.error('Erro ao adicionar aluno:', error);
      }
    );
  }
}
