import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-login',
  templateUrl: 'login.page.html',
  styleUrls: ['login.page.scss'],
})
export class LoginPage {
  username: string = '';
  password: string = '';

  constructor(private router: Router, private http: HttpClient) {}

  onSubmit() {
    const loginData = {
      username: this.username,
      password: this.password,
    };

    // Enviar os dados para a API Django
    this.http.post<any>('http://127.0.0.1:8000/api/login/', loginData).subscribe(
      (response) => {
        // Salvar o token no localStorage ou outro mecanismo de armazenamento
        localStorage.setItem('auth_token', response.token);
        console.log('Login bem-sucedido');
        this.router.navigate(['/home-page']); // Redirecionar para a página principal
      },
      (error) => {
        console.error('Erro no login', error);
        alert('Credenciais inválidas');
      }
    );
  }
}
