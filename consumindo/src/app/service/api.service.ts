import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { Router } from '@angular/router';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private url: string = "http://127.0.0.1:8000/api/alunos";
  private urlCampusCursos: string = "http://127.0.0.1:8000/api/campusCursos/";
  
  constructor(private http: HttpClient,  private router: Router) { }

  getData(): Observable<any[]> { // Atualize o tipo de retorno aqui
    return this.http.get<any[]>(this.url); // Especifique o tipo na chamada do HttpClient
  }

  getCampusCursos(): Observable<any[]> {
    return this.http.get<any[]>(this.urlCampusCursos);
  }

  deleteAluno(id: number): Observable<any> {
    const url = `http://127.0.0.1:8000/api/alunos/${id}/`;
    return this.http.delete(url);
  }

  addAluno(aluno: any): Observable<any> {
    const url = "http://127.0.0.1:8000/api/adicionarAluno/";
    return this.http.post(url, aluno);
  }

  getCursos(): Observable<any[]> {
    const url = "http://127.0.0.1:8000/api/cursos/"; // Substitua pelo endpoint correto da sua API
    return this.http.get<any[]>(url);
  }
  
  getSituacoes(): Observable<any[]> {
    const url = "http://127.0.0.1:8000/api/situacoes/"; // Substitua pelo endpoint correto da sua API
    return this.http.get<any[]>(url);
  }

  getFormasIngresso(): Observable<any[]> {
    const url = "http://127.0.0.1:8000/api/formas-ingresso/"; // Substitua pelo endpoint correto
    return this.http.get<any[]>(url);
  }

  updateAluno(id: string, aluno: any): Observable<any> {
    const url = `http://127.0.0.1:8000/api/editarAluno/${id}/`;
    return this.http.patch<any>(url, aluno);
  }

}
