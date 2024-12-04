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
  }

  getAluno(id: string) {
    this.apiService.getData().subscribe((alunos: any[]) => {
      this.aluno = alunos.find(a => a.id === parseInt(id)); // Encontre o aluno pelo ID
    });
  }

  updateAluno() {
    this.apiService.updateAluno(this.aluno.id, this.aluno).subscribe(response => {
      console.log('Aluno atualizado', response);
      this.navCtrl.back(); // Volta para a página anterior após atualizar
    }, error => {
      console.error('Erro ao atualizar aluno', error);
    });
  }
}
