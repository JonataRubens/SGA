import { Component, OnInit } from '@angular/core';
import { ApiService } from './../service/api.service';

@Component({
  selector: 'app-about',
  templateUrl: './about.page.html',
  styleUrls: ['./about.page.scss'],
})
export class AboutPage implements OnInit {
  campusCursos: any[] = []; // Definindo a variável para armazenar os dados dos campus e cursos

  constructor(private apiService: ApiService) { }

  ngOnInit() {
    this.getCampusCursos(); // Chama a função para buscar os dados
  }

  getCampusCursos() {
    this.apiService.getCampusCursos().subscribe(
      (data: any[]) => {
        console.log(data); // Verifique se os dados estão corretos
        this.campusCursos = data; // Armazene os dados
      },
      error => {
        console.error('Erro ao carregar os dados dos campus e cursos:', error);
      }
    );
  }
}
