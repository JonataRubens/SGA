import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';

@Component({
  selector: 'app-home-page',
  templateUrl: './home-page.page.html',
  styleUrls: ['./home-page.page.scss'],
})
export class HomePagePage implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {}

  logout() {
    localStorage.removeItem('auth_token');
    this.router.navigate(['/login']);
  }
}
