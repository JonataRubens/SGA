import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private url: string = "http://127.0.0.1:8000/api/alunos";
  private urlCampusCursos: string = "http://127.0.0.1:8000/api/campus-cursos/";
  
  constructor(private http: HttpClient) { }

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
}
