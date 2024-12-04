import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from '../service/api.service';
import { NavController } from '@ionic/angular';

@Component({
  selector: 'app-editar-aluno',
  templateUrl: './editar-aluno.page.html',
  styleUrls: ['./editar-aluno.page.scss'],
})
export class EditarAlunoPage implements OnInit {
  aluno: any = {};
  cursos: any[] = [];
  situacoes: any[] = [];

  constructor(
    private activatedRoute: ActivatedRoute,
    private apiService: ApiService,
    private navCtrl: NavController
  ) {}

  ngOnInit() {
    const alunoId = this.activatedRoute.snapshot.paramMap.get('id');
    if (alunoId !== null) {
      this.getAluno(alunoId);
    }

    this.getCursos();
    this.getSituacoes();
  }

  getAluno(id: string) {
    this.apiService.getData().subscribe((alunos: any[]) => {
      this.aluno = alunos.find(a => a.id === parseInt(id));
      // Remova qualquer dado que não seja necessário para o PATCH
      this.aluno = {
        id: this.aluno.id,
        nomeCompleto: this.aluno.nomeCompleto,
        cpf: this.aluno.cpf,
        curso_id: this.aluno.curso.id,
        situacao_id: this.aluno.situacao.id,
      };
    });
  }
  

  getCursos() {
    this.apiService.getCursos().subscribe(data => {
      this.cursos = data;
    });
  }

  getSituacoes() {
    this.apiService.getSituacoes().subscribe(data => {
      this.situacoes = data;
    });
  }

  updateAluno() {
    console.log('Dados enviados:', this.aluno); // Log dos dados enviados
    this.apiService.updateAluno(this.aluno.id, this.aluno).subscribe(
      response => {
        console.log('Aluno atualizado', response);
        this.navCtrl.back(); // Volta para a página anterior após atualizar
      },
      error => {
        console.error('Erro ao atualizar aluno', error);
      }
    );
  }
}
